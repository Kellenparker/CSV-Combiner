import pytest
import pandas as pd
import datatest as dt
from math import isnan

# Load all sub CSVs by relative path and give them a filename column for testing
sub1 = pd.read_csv("fixtures/accessories.csv")
sub1['filename'] = "accessories.csv"
sub2 = pd.read_csv("fixtures/clothing.csv")
sub2['filename'] = "clothing.csv"
sub3 = pd.read_csv("fixtures/household_cleaners.csv")
sub3['filename'] = "household_cleaners.csv"


# Load the combined CSV file by relative path
@pytest.fixture(scope='session')
@dt.working_directory(__file__)
def df():
    return pd.read_csv('combined.csv')


# Test if the combined CSV has all expected column names
@pytest.mark.mandatory
def test_column_names(df):
    required_names = {'email_hash', 'category', 'filename'}
    dt.validate(df.columns, required_names)


# Test if the input CSV files are all subsets of the combined CSV
def test_subset(df):
    assert (len(df.merge(sub1)) == len(sub1))
    df.merge(sub1)
    assert (len(df.merge(sub2)) == len(sub2))
    df.merge(sub2)
    assert (len(df.merge(sub3)) == len(sub3))


# Test if the sum of the length of the input CSV files are equal to the length of the output combined CSV
def test_len(df):
    assert (len(df) == len(sub1) + len(sub2) + len(sub3))

if __name__ == '__main__':
    import sys
    sys.exit(pytest.main(sys.argv[0]))