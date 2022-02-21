"""Ensure the types of a pandas DataFrame are correct."""

from abc import ABC
from dataclasses import dataclass
from typing import (
    Callable,
    Optional,
    Union,
)

from loguru import logger
from numpy import dtype
from pandas import DataFrame, Series

# Set up on Git
# ToDo: Write tests (pytest)
# ToDo: Find and use appropriate cookiecutter (cthoyt/cookiecutter-snekpack)
# ToDo: Set up tox with pytest, flake8
# ToDo: Package leveraging tox
# ToDo: Add tox-battery

# Be stricter with TypeDict
# ToDo: Add beartype to type_dict.
# ToDo: Add type hints to all methods.
# ToDo: Add column name recognition (KeyError) as exception in typecheck

# Clean up
# ToDo: Finish error checks in TypeDict.
# ToDo: Finish type hints
# ToDo: Standardise docstrings

# logger research
# ToDo: Find the best way to handle logger, to avoid unclosed log connection
# ToDo: Warning/error logger levels (use enum)


class TypeCheckError(Exception):
    """Custom error to catch failed type checks.

    Raised if columns are incorrectly typed, or are not in the type_dict.
    """


@dataclass
class TypeCheckLogger(ABC):
    """Log TypeCheck errors."""

    typecheck_logger: Callable = logger.error
    warning_mode: bool = False

    def log_missing_cols(self, missing_cols: dict) -> None:
        """Log missing cols."""
        self.typecheck_logger('Columns with no specified type:')
        for col_name, col_type in missing_cols.items():
            self.typecheck_logger(
                '\t{col_name}: {col_type}'.format(
                    col_name=col_name, col_type=col_type,
                ),
            )

    def log_incorrect_cols(self, incorrect_cols: dict) -> None:
        """Log incorrect cols.

        Args:
            incorrect_cols (dict):
                keys: string
                values: dict[type_of_df:class, correct_type:class]
        """
        self.typecheck_logger('Columns with incorrect types:')
        for col_name, row in incorrect_cols.items():
            log_string = '{col_name} is {col_type}, should be {correct_type}'
            log_string = log_string.format(
                col_name=col_name,
                col_type=row['type_in_df'],
                correct_type=row['correct_type'],
            )
            self.typecheck_logger(log_string)

    def log_failed_typecheck(
        self,
        missing_cols: dict,
        incorrect_cols: dict,
        stage: Optional[str] = None,
    ) -> None:
        """Print the output of a failed type check."""
        if missing_cols:
            self.log_missing_cols(missing_cols)

        if incorrect_cols:
            self.log_incorrect_cols(incorrect_cols)

        if stage is not None:
            message = 'typecheck failed at stage: {stage}'.format(stage=stage)
        else:
            message = 'typecheck failed'

        if not self.warning_mode:
            raise TypeCheckError(message)


class TypeDict(TypeCheckLogger):
    """Type check and add functionality to a type_dict."""

    def __init__(
        self,
        type_dict: dict[str, Union[type, dtype, str]],
        typecheck_logger: Callable = logger.error,
        warning_mode: bool = False,
    ) -> None:
        """Initialise TypeDict."""
        self.type_dict = type_dict
        super().__init__(typecheck_logger, warning_mode)

    def get(self):
        """Get the type dict."""
        return self.type_dict

    def type_dict_subset(self, cols):
        """Generate subset of type dict eg for mass astype."""
        return {col: self.type_dict[col] for col in cols}

    def typechecker(self, df_types: dict, stage: Optional[str] = None) -> None:
        """Check a Pandas DataFrame's types match a type dictionary."""
        missing_cols = {}
        incorrect_cols = {}

        for col, col_type in df_types.items():
            if col not in self.type_dict:
                missing_cols[col] = col_type
                continue
            if col_type != self.type_dict[col]:
                incorrect_cols[col] = {
                    'type_in_df': col_type,
                    'correct_type': self.type_dict[col],
                }
        if missing_cols or incorrect_cols:
            self.log_failed_typecheck(missing_cols, incorrect_cols, stage)

    def make_typecheck(self) -> Callable:
        """Type check decorator for a single-df transformation."""
        def decorator(func: Callable) -> Callable:
            """Decorator for checking types."""
            def wrapper(
                df: Optional[DataFrame] = None, *args, **kwargs,
            ) -> Callable:
                """Wrapper for typechecking functions."""
                if isinstance(df, DataFrame):
                    self.typechecker(df.dtypes.to_dict(), 'input')
                    output_df = func(df, *args, **kwargs)
                else:
                    output_df = func(*args, **kwargs)
                self.typechecker(output_df.dtypes, 'output')
                return output_df
            return wrapper
        return decorator


class DataFrameTypeDictTools(TypeDict):
    """Helps build and handle types in dataframes."""

    def df_from_dict(self, input_dict):
        """
        Create type strict df from input dict.

        ToDo: Handle case when col is not in type dict.
        ToDo: Handle case when not same number of cols as col names.
        ToDo: Handle case when dicts have different list lengths?
        Above case should be handled by pandas.
        """
        df_series = {
            key: Series(col, dtype=self.type_dict[key])
            for key, col in input_dict.items()
        }
        return DataFrame(df_series)

    def df_from_list_of_lists(self, list_of_lists, cols, transpose=False):
        """
        Create df from list of lists.

        ToDo: handle case when input isn't rectangular.
        """
        if transpose:
            list_of_lists = list(map(list, zip(*list_of_lists)))

        input_dict = dict(zip(cols, list_of_lists))
        return self.df_from_dict(input_dict)

    def mass_astype(self, df):
        """
        Mass astype using type_dict.

        ToDo: Consider KeyError.
        """
        return df.astype(self.type_dict_subset(df.columns))
