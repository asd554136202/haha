from openpyxl import load_workbook

local = './test.xlsx'

wb = load_workbook(local)

ws = wb['Sheet1']



