import argparse
import sys
import pandas as pd

parser = argparse.ArgumentParser(description='Convert xlsx file to csv')
parser.add_argument('file', type=str, help='xlsx file to convert')
parser.add_argument('--verbose', action='store_true', help='Print verbose messages')
args = parser.parse_args()

def main():
    assert args.file.endswith('.xlsx'), 'File must be xlsx format'

    xlsx_file = args.file
    if args.verbose: print(f'Converting file: {xlsx_file} to csv')

    for sheet in pd.read_excel(xlsx_file, sheet_name=None, dtype=str):
        print(sheet)
        if args.verbose: print(pd.read_excel(xlsx_file, sheet_name=sheet, dtype=str).head())

        pd.read_excel(xlsx_file, sheet_name=sheet).to_csv(f'{xlsx_file}_{sheet}.csv', index=False)
        print(f'File {xlsx_file}_{sheet}.csv has been created')

if __name__ == '__main__':
    main()

