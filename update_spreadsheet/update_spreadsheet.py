import openpyxl
import os
for name in os.listdir('source_files'):
    workbook = openpyxl.load_workbook(filename='source_files/' + name)
    sheet = workbook['Sheet1']
    sheet['C1'].value = 'Next age'
    for row in range(2, 100):
        if sheet[f'B{row}'].value:
            sheet[f'C{row}'].value = sheet[f'B{row}'].value + 1
    workbook.save(filename='target_files/' + name)
