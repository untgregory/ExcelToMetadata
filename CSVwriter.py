import openpyxl
import csv

# change the xlsx filename depending on which workbook is being imported from the Metadata folder
wb = openpyxl.load_workbook('S:\\Digitization\\Metadata\\MS361_LewisScrapbook.xlsx', data_only = True)
sh1 = wb["MODS"]
with open('S:\\Digitization\\Metadata\\tools\\CSVs\\MODS.csv', 'w', newline='') as f:
	c = csv.writer(f)
	for r in sh1.rows:
		out_val_list = list()
		for cell in r:
			out_val = cell.value
			if out_val == 0:
				out_val = ""
			out_val_list.append(out_val)
		c.writerow(out_val_list)

sh2 = wb["DC"]
with open('S:\\Digitization\\Metadata\\tools\\CSVs\\DC.csv', 'w', newline='') as f:
	c = csv.writer(f)
	for r in sh2.rows:
		out_val_list = list()
		for cell in r:
			out_val = cell.value
			if out_val == 0:
				out_val = ""
			out_val_list.append(out_val)
		c.writerow(out_val_list)
		
sh3 = wb["IPTC"]
with open('S:\\Digitization\\Metadata\\tools\\CSVs\\IPTC.txt', 'w', newline='') as f:
	c = csv.writer(f, delimiter='\t')
	for r in sh3.rows:
		out_val_list = list()
		for cell in r:
			out_val = cell.value
			if out_val == 0:
				out_val = ""
			out_val_list.append(out_val)
		c.writerow(out_val_list)
