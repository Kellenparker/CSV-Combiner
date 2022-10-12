# CSV Combiner

This script takes multiple CSV files and combines them into one.

## Requirements
- Python 3.6+

- pandas
```
$ pip install pandas
```
- pytest (For testing)
```
$ pip install pytest
```
- datatest (For testing)
```
$ pip install datatest
```

## Installation

```
$ git clone https://github.com/Kellenparker/CSV-Combiner.git
```

Please make sure all dependencies are installed before running.

## Usage
Naming each input file individually:
```
$ python3 csv_combiner.py input_1.csv input_2.csv ... input_n.csv > combined.csv
```

Using a folder containing all of the input files:
```
$ python3 csv_combiner.py input/ > combined.csv
```

## Dependencies
### pandas (1.5.0)
Used to handle, modify, and combine CSV files
### pytest (7.1.3) (Testing only)
Used to run unit tests
### datatest (0.11.1) (Testing only)
Allowed the use of more data appropriate testing functions

## Example

Given two input files named `clothing.csv` and `accessories.csv` in a folder named `fixtures`.
```
$ python3 csv_combiner.py fixtures/clothing.csv fixtures/accessories.csv > combined.csv
```

clothing.csv:

|email_hash|category|
|----------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|

accessories.csv:

|email_hash|category|
|----------|--------|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|

combined.csv:

|email_hash|category|filename|
|----------|--------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|clothing.csv|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|clothing.csv|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|clothing.csv|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|accessories.csv|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|accessories.csv|

## Unit Testing

Unit testing can be performed via combiner_test.py. The unit tests will cover various aspects to ensure that the combined .csv file contains all the information from the seperate .csv files and nothing more.

### Usage

All file paths are hard coded into the file and will need to be changed depending on the test case.

To run the unit test:
```
$ pytest combiner_test.py
```
Or:
```
$ python3 -m pytest combiner_test.py
```
Note: pytest and datatest are required for running the tests.

## Assumptions

- If `filename` is already included as a column in an input file, a new `filename` column will not be created for that file.
- Since no key is inputted, data will not be merged.