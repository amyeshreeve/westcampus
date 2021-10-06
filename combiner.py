import os
import pandas as pd

years = [1880, 1900, 1910, 1920]

for year in years:
	yearn = str(year)
	filename1 = yearn + ".xlsx"
	filename2 = "W" + filename1
	filename3 = "F" + filename1
	file1 = pd.ExcelFile(filename1)
	df1 = pd.read_excel(file1, 'HOH')
	file2 = pd.ExcelFile(filename2)
	df2 = pd.read_excel(file2, 'HOH')
	df1 = df1[["Given Name", "Surname", "C_FULL_AD"]]
	df2 = df2[["Given Name", "Surname", "C_FULL_AD"]]
	df3 = pd.concat([df1, df2])
	df3.to_excel(filename3)