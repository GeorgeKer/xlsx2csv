import pandas as pd
import sys

def main():
    args = sys.argv[1:]
    assert len(args) == 1, 'Please provide a file name'
    
    xlsx_file = args[0]
    print(f'Converting file: {xlsx_file} to csv')

    for sheet in pd.read_excel(xlsx_file, sheet_name=None, dtype=str):
        print(sheet)
        print(pd.read_excel(xlsx_file, sheet_name=sheet, dtype=str))
        pd.read_excel(xlsx_file, sheet_name=sheet).to_csv(f'{xlsx_file}_{sheet}.csv', index=False)
        print(f'File {xlsx_file}_{sheet}.csv has been created')

if __name__ == '__main__':
    main()

