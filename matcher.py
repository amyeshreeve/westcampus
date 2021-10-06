import os
import pandas as pd

years = [1880, 1900, 1910, 1920]

home = str(input('Enter your plain street address:'))
print("In 2021, you live at", home)

for year in years:
	yearn = str(year)
	filename = "F" + yearn + ".xlsx"
	sheet = pd.read_excel(filename)
	rows = sheet.loc[sheet['C_FULL_AD'].str.contains(home, case=False, na=False)]
	if rows.empty:
		print("Nobody lived there in", year)
	elif rows.shape[0] >= 2:
		num = rows.shape[0]
		if num >= 3:
			txt = ", and "
		else:
			txt = " and "
		print("In ", year, ", ", end = "", sep = "")
		while num > 0:
			rows = rows.reset_index(drop=True)
			first = rows.iloc[0]['Given Name']
			last = rows.iloc[0]['Surname']
			if num == 1:
				print(first, last, "lived at", home)
			if num == 2:
				print(first, " ", last, txt, end = "", sep = "")
			if num > 2:	
				print(first, " ", last, ", ", end = "", sep = "")
			rows = rows.drop(0)
			num -= 1

	elif rows.shape[0] == 1:
		first = rows['Given Name'].item()
		last = rows['Surname'].item()
		print("In", year, first, last, "lived at", home)
		