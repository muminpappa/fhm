# upload to MySQL
import xlrd

fn = 'fhm_download_2020-11-13.xlsx'

wb = xlrd.open_workbook(filename=fn)
print('Importing from sheet ' + wb.sheet_names()[0] + ' in file ' + fn)
sheet = wb.sheet_by_name(wb.sheet_names()[0])
print(wb.sheet_by_index(wb.nsheets-1).cell_value(1, 0))
