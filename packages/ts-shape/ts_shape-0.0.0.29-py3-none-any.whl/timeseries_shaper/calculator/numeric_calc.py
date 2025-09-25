import pandas as pd
from ..base import Base

class IntegerCalc(Base):
    """
    Provides class methods for performing calculations on integer columns in a pandas DataFrame.
    """

    @classmethod
    def scale_column(cls, dataframe: pd.DataFrame, column_name: str = 'value_integer', factor: float = 1) -> pd.DataFrame:
        """
        Scales the integer column by the given factor.

        Args:
            dataframe (pd.DataFrame): The DataFrame to perform the operation on.
            column_name (str): The column to apply the scaling to.
            factor (float): The scaling factor.

        Returns:
            pd.DataFrame: The DataFrame with the scaled column.
        """
        dataframe[column_name] = dataframe[column_name] * factor
        return dataframe

    @classmethod
    def offset_column(cls, dataframe: pd.DataFrame, column_name: str = 'value_integer', offset_value: float = 0) -> pd.DataFrame:
        """
        Offsets the integer column by the given value.

        Args:
            dataframe (pd.DataFrame): The DataFrame to perform the operation on.
            column_name (str): The column to apply the offset to.
            offset_value (float): The value to add (positive) or subtract (negative) from each element in the column.

        Returns:
            pd.DataFrame: The DataFrame with the offset column.
        """
        dataframe[column_name] = dataframe[column_name] + offset_value
        return dataframe

    @classmethod
    def divide_column(cls, dataframe: pd.DataFrame, column_name: str = 'value_integer', divisor: float = 1) -> pd.DataFrame:
        """
        Divides each value in the integer column by the given divisor.

        Args:
            dataframe (pd.DataFrame): The DataFrame to perform the operation on.
            column_name (str): The column to apply the division to.
            divisor (float): The value by which to divide each element.

        Returns:
            pd.DataFrame: The DataFrame with the divided column.
        """
        dataframe[column_name] = dataframe[column_name] / divisor
        return dataframe

    @classmethod
    def subtract_column(cls, dataframe: pd.DataFrame, column_name: str = 'value_integer', subtract_value: float = 0) -> pd.DataFrame:
        """
        Subtracts a given value from each element in the integer column.

        Args:
            dataframe (pd.DataFrame): The DataFrame to perform the operation on.
            column_name (str): The column to apply the subtraction to.
            subtract_value (float): The value to subtract from each element.

        Returns:
            pd.DataFrame: The DataFrame with the subtracted column.
        """
        dataframe[column_name] = dataframe[column_name] - subtract_value
        return dataframe

    @classmethod
    def calculate_with_fixed_factors(cls, dataframe: pd.DataFrame, column_name: str = 'value_integer', multiply_factor: float = 1, add_factor: float = 0) -> pd.DataFrame:
        """
        Performs a calculation by multiplying with a factor and then adding an additional factor.

        Args:
            dataframe (pd.DataFrame): The DataFrame to perform the operation on.
            column_name (str): The column to apply the calculations to.
            multiply_factor (float): The factor to multiply each value by. Defaults to 1 (no scaling).
            add_factor (float): The value to add after multiplication. Defaults to 0 (no offset).

        Returns:
            pd.DataFrame: The DataFrame after applying the calculations.
        """
        dataframe[column_name] = (dataframe[column_name] * multiply_factor) + add_factor
        return dataframe

    @classmethod
    def mod_column(cls, dataframe: pd.DataFrame, column_name: str = 'value_integer', mod_value: int = 1) -> pd.DataFrame:
        """
        Performs a modulus operation on the integer column with a specified value.

        Args:
            dataframe (pd.DataFrame): The DataFrame to perform the operation on.
            column_name (str): The column to apply the modulus operation to.
            mod_value (int): The value to perform the modulus operation with.

        Returns:
            pd.DataFrame: The DataFrame with the modulus operation applied.
        """
        dataframe[column_name] = dataframe[column_name] % mod_value
        return dataframe

    @classmethod
    def power_column(cls, dataframe: pd.DataFrame, column_name: str = 'value_integer', power_value: float = 1) -> pd.DataFrame:
        """
        Raises each value in the integer column to the power of a specified value.

        Args:
            dataframe (pd.DataFrame): The DataFrame to perform the operation on.
            column_name (str): The column to apply the power operation to.
            power_value (float): The exponent to raise each element to.

        Returns:
            pd.DataFrame: The DataFrame with the power operation applied.
        """
        dataframe[column_name] = dataframe[column_name] ** power_value
        return dataframe