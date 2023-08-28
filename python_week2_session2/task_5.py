import re
import openpyxl
def parse_header_file(header_file):
    with open(header_file, 'r') as f:
        content = f.read()

    pattern = r'(\w+\s+\w+\s*\([^)]*\)\s*;)'
    prototypes = re.findall(pattern, content)
    return prototypes

def main():
    header_file = 'D:/Embedded/Embedded Liniux Diploma/Python_Tasks/firefox_task/gpio.h'
    prototypes = parse_header_file(header_file)

    if prototypes:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet['A1'] = 'Function Prototypes'
        sheet['B1'] = 'Function ID'

        for idx, (function_name) in enumerate(prototypes, start=0):
         cell_id = f'IDX0{idx}'
         sheet[f'B{idx + 2}'] = cell_id
         sheet[f'A{idx + 2}'] = function_name


        excel_file = 'function_prototypes.xlsx'
        workbook.save(excel_file)
        print(f'Function prototypes saved to {excel_file}')
    else:
        print('No function prototypes found.')

if __name__ == '__main__':
    main()

