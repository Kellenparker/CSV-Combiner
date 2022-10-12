import pandas as pd
import os
import sys
import glob

# Function: csv_combiner()
# Purpose: Take two or more csv files and convert them into one
# Returns: DataFrame of the combined csv files
def csv_combiner():
    inputAr = [] # Array to hold the DataFrames for all csv files
    for input in sys.argv[1:]:
        if os.path.isdir(input):  # Check if input is a directory
            files = glob.glob(os.path.join(input, "*.csv"))
            for file in files:
                inputAr.append(import_file(file))
        elif os.path.isfile(input):  # Check if input is a file
            inputAr.append(import_file(input))
        else:
            print(f'INPUT: {input} is not a valid file or directory')
            sys.exit()

    # Merge the csv files in inputAr
    df = pd.concat(inputAr, axis=0, ignore_index=True)
    sys.stdout.write(df.to_csv(index=False))
    return df

# Function: import_file(filePath)
# Purpose: Import a csv file as a dataframe given its path
# Params: filePath - a relative path to a csv file
# Returns: DataFrame of the single csv file, with added column "filename" containing the file name
def import_file(filePath) -> pd.DataFrame:
    # Test file to catch common exceptions
    try:
        df = pd.read_csv(filePath, index_col=None, header=0)
    except FileNotFoundError:
        print(f'FILE: {filePath} is not found')
        sys.exit()
    except pd.errors.EmptyDataError:
        print(f'FILE: {filePath} is empty')
        sys.exit()
    except pd.errors.ParserError:
        print(f'FILE: {filePath} is cannot be parsed')
        sys.exit()

    # Add filename column if it does not already exist
    if 'filename' not in df.columns:
        df['filename'] = os.path.basename(filePath)

    return df

if __name__ == "__main__":
    csv_combiner()