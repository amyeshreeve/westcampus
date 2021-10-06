import os
import pandas as pd

years = [1880, 1900, 1910, 1920, 1930]

home = str(input('Enter your plain street address:'))
print("In 2021, you live at", home)

for year in years:
	years = str(year)
	filename = years + ".xlsx"
	file = pd.ExcelFile(filename)
	sheet = pd.read_excel(file, 'HOH')
	sheet['C_FULL_ADD'] = sheet['C_FULL_ADD'].fillna('')
	rows = sheet.loc[sheet['C_FULL_ADD'].str.contains(home, case=False)]
	if rows.empty:
		print("Nobody lived there in", year)
	else:
		first = rows['Given Name'].item()
		last = rows['Surname'].item()
		print("In", year, first, last, "lived at", home)