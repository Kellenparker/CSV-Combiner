import pytest
import pandas as pd
import datatest as dt
from math import isnan

# Load all sub CSVs by relative path and give them a filename column for testing
# **** Change these files as needed ****
inputFiles = []
input = pd.read_csv("fixtures/accessories.csv")
input['filename'] = "accessories.csv"
inputFiles.append(input)
input = pd.read_csv("fixtures/clothing.csv")
input['filename'] = "clothing.csv"
inputFiles.append(input)
input = pd.read_csv("fixtures/household_cleaners.csv")
input['filename'] = "household_cleaners.csv"
inputFiles.append(input)

# **** Change column names as needed ****
column_names = {'email_hash', 'category', 'filename'}


# Load the combined CSV file by relative path
@pytest.fixture(scope='session')
@dt.working_directory(__file__)
def df():
    # **** Change combined CSV file name as needed ****
    return pd.read_csv('combined.csv')


# Test if the combined CSV has all expected column names
@pytest.mark.mandatory
def test_column_names(df):
    dt.validate(df.columns, column_names)


# Test if the input CSV files are all subsets of the combined CSV
def test_subset(df):
    for file in inputFiles:
        assert (len(df.merge(file)) == len(file))
        df.merge(file)


# Test if the sum of the length of the input CSV files are equal to the length of the output combined CSV
def test_len(df):
    sumLen = 0
    for file in inputFiles:
        sumLen += len(file)
    assert (len(df) == sumLen)

if __name__ == '__main__':
    import sys
    sys.exit(pytest.main(sys.argv[0]))