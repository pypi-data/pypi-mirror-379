import pandas as pd
from ..base import Base

class StringFilter(Base):
    """
    A class for filtering operations on string columns within a pandas DataFrame.
    
    Provides class methods for operations on string columns.
    """

    @classmethod
    def filter_na_value_string(cls, dataframe: pd.DataFrame, column_name: str = 'value_string') -> pd.DataFrame:
        """Filters out rows where the specified string column is NA."""
        return dataframe[dataframe[column_name].notna()]

    @classmethod
    def filter_value_string_match(cls, dataframe: pd.DataFrame, string_value: str, column_name: str = 'value_string') -> pd.DataFrame:
        """Filters rows where the specified string column matches the provided string."""
        return dataframe[dataframe[column_name] == string_value]

    @classmethod
    def filter_value_string_not_match(cls, dataframe: pd.DataFrame, string_value: str, column_name: str = 'value_string') -> pd.DataFrame:
        """Filters rows where the specified string column does not match the provided string."""
        return dataframe[dataframe[column_name] != string_value]

    @classmethod
    def filter_string_contains(cls, dataframe: pd.DataFrame, substring: str, column_name: str = 'value_string') -> pd.DataFrame:
        """Filters rows where the specified string column contains the provided substring."""
        return dataframe[dataframe[column_name].str.contains(substring, na=False)]

    @classmethod
    def regex_clean_value_string(cls, dataframe: pd.DataFrame, column_name: str = 'value_string', regex_pattern: str = r'(\d+)\s*([a-zA-Z]*)', replacement: str = '', regex: bool = True) -> pd.DataFrame:
        """Applies a regex pattern to clean the specified string column."""
        dataframe[column_name] = dataframe[column_name].str.replace(regex_pattern, replacement, regex=regex)
        return dataframe

    @classmethod
    def detect_changes_in_string(cls, dataframe: pd.DataFrame, column_name: str = 'value_string') -> pd.DataFrame:
        """Detects changes from row to row in the specified string column."""
        changes_detected = dataframe[column_name].ne(dataframe[column_name].shift())
        result = dataframe[changes_detected]
        if result.empty:
            print(f"No changes detected in the '{column_name}' column between consecutive rows.")
        return result
