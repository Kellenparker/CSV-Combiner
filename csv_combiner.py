import pandas as pd
import os
import sys
import glob

def main():
    inputAr = []
    for input in sys.argv[1:]:
        if os.path.isdir(input):  # Check if input is a directory
            files = glob.glob(os.path.join(input, "*.csv"))
            for file in files:
                inputAr.append(importFile(file))
        elif os.path.isfile(input):  # Check if input is a file
            inputAr.append(importFile(input))
        else:
            print(f'INPUT: {input} is not a valid file or directory')
            sys.exit()

    df = pd.concat(inputAr, axis=0, ignore_index=True)
    print(type(df))
    sys.stdout.write(df.to_csv())


def importFile(filePath) -> pd.DataFrame:
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
    main()