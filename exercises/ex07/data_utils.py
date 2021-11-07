"""Utility functions."""

__author__ = "730214639"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the datafile into the Jupyter file."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list of values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-table to a column-table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(col_table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produces the first "n" rows of a table."""
    result: dict[str, list[str]] = {}
    if number_of_rows >= len(col_table):
        return col_table
    else:
        for column in col_table:
            empty_list = []
            for i in range(number_of_rows):
                empty_list.append(col_table[column][i])
            result[column] = empty_list
    return result


def select(col_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Choosing columns you want to analyze."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = col_table[column]
    return result


def concat(col_table1: dict[str, list[str]], col_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two dictionaries."""
    result: dict[str, list[str]] = {}
    for column in col_table1:
        result[column] = col_table1[column]
    for column in col_table2:
        if column in result:
            result[column] += col_table2[column]
        else: 
            result[column] = col_table2[column]
    return result


def count(list: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a dictionary."""
    result: dict[str, int] = {}
    for item in list:
        if item in result:
            result[item] += 1
        if item not in result:
            result[item] = 1
        
    return result