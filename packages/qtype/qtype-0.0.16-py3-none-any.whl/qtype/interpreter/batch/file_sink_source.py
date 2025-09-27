from typing import Any, Tuple

import fsspec  # type: ignore[import-untyped]
import pandas as pd

from qtype.base.exceptions import InterpreterError
from qtype.interpreter.batch.types import BatchConfig, ErrorMode
from qtype.interpreter.batch.utils import reconcile_results_and_errors
from qtype.semantic.model import FileSink, FileSource


def execute_file_source(
    step: FileSource,
    inputs: pd.DataFrame,
    batch_config: BatchConfig,
    **kwargs: dict[Any, Any],
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Executes a FileSource step to read data from a file using fsspec.

    Args:
        step: The FileSource step to execute.
        inputs: Input DataFrame (may contain path variable).
        batch_config: Configuration for batch processing.
        **kwargs: Additional keyword arguments.

    Returns:
        A tuple containing two DataFrames:
            - The first DataFrame contains the successfully read data.
            - The second DataFrame contains rows that encountered errors with an 'error' column.
    """
    output_columns = {output.id for output in step.outputs}

    results = []
    errors = []

    # FileSource has cardinality 'many', so it reads once and produces multiple output rows
    # We process each input row (which might have different paths) separately
    for _, row in inputs.iterrows():
        try:
            file_path = step.path if step.path else row.get("path")
            if not file_path:
                raise InterpreterError(
                    f"No path specified for {type(step).__name__}. "
                    "Either set the 'path' field or provide a 'path' input variable."
                )

            # Use fsspec to open the file and read with pandas
            with fsspec.open(file_path, "rb") as file_handle:
                df = pd.read_parquet(file_handle)  # type: ignore[arg-type]

            # Filter to only the expected output columns if they exist
            if output_columns and len(df) > 0:
                available_columns = set(df.columns)
                missing_columns = output_columns - available_columns
                if missing_columns:
                    raise InterpreterError(
                        f"File {file_path} missing expected columns: {', '.join(missing_columns)}. "
                        f"Available columns: {', '.join(available_columns)}"
                    )
                df = df[[col for col in df.columns if col in output_columns]]

            results.append(df)

        except Exception as e:
            if batch_config.error_mode == ErrorMode.FAIL:
                raise e

            # If there's an error, add it to the errors list
            error_df = pd.DataFrame([{"error": str(e)}])
            errors.append(error_df)

    return reconcile_results_and_errors(results, errors)


def execute_file_sink(
    step: FileSink,
    inputs: pd.DataFrame,
    batch_config: BatchConfig,
    **kwargs: dict[Any, Any],
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Executes a FileSink step to write data to a file using fsspec.

    Args:
        step: The FileSink step to execute.
        inputs: Input DataFrame containing data to write.
        batch_config: Configuration for batch processing.
        **kwargs: Additional keyword arguments.

    Returns:
        A tuple containing two DataFrames:
            - The first DataFrame contains success indicators.
            - The second DataFrame contains rows that encountered errors with an 'error' column.
    """
    # this is enforced by the dsl, but we'll check here to confirm
    if len(step.outputs) > 1:
        raise InterpreterError(
            f"There should only be one output variable for {type(step).__name__}."
        )
    output_column_name = step.outputs[0].id

    # make a list of all file paths
    try:
        if step.path:
            file_paths = [step.path] * len(inputs)
        else:
            if "path" not in inputs.columns:
                raise InterpreterError(
                    f"No path specified for {type(step).__name__}. "
                    "Either set the 'path' field or provide a 'path' input variable."
                )
            file_paths = inputs["path"].tolist()
    except Exception as e:
        if batch_config.error_mode == ErrorMode.FAIL:
            raise e
        # If we can't get the path, we can't proceed
        return pd.DataFrame(), pd.DataFrame([{"error": str(e)}])

    # Check if all paths are the same
    unique_paths = list(set(file_paths))

    if len(unique_paths) == 1:
        # All rows write to the same file - process as one batch
        file_path = unique_paths[0]

        try:
            # Use fsspec to write the parquet file
            input_columns = [i.id for i in step.inputs]
            with fsspec.open(file_path, "wb") as file_handle:
                inputs[input_columns].to_parquet(file_handle, index=False)  # type: ignore[arg-type]

            inputs[output_column_name] = file_path
            return inputs, pd.DataFrame()

        except Exception as e:
            if batch_config.error_mode == ErrorMode.FAIL:
                raise e

            # If there's an error, return error for all rows
            error_df = pd.DataFrame([{"error": str(e)}])
            return pd.DataFrame(), error_df

    else:
        # Multiple unique paths - split inputs and process recursively
        all_results = []
        all_errors = []

        for unique_path in unique_paths:
            # Create mask for rows with this path
            path_mask = [p == unique_path for p in file_paths]
            sliced_inputs = inputs[path_mask].copy()

            # Recursively call execute_file_sink with the sliced DataFrame
            results, errors = execute_file_sink(
                step, sliced_inputs, batch_config, **kwargs
            )

            if len(results) > 0:
                all_results.append(results)
            if len(errors) > 0:
                all_errors.append(errors)

        return reconcile_results_and_errors(all_results, all_errors)
