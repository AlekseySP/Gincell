from openpyxl import load_workbook
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import Font, Alignment
from openpyxl import Workbook
from datetime import datetime

import os

d = datetime.now()

fontStyle = Font(size = "18", bold=True)

thin_border = Border(left=Side(style='thin'), 
                     right=Side(style='thin'), 
                     top=Side(style='thin'), 
                     bottom=Side(style='thin'))

thick_border = Border(left=Side(style='thick'), 
                     right=Side(style='thick'), 
                     top=Side(style='thick'), 
                     bottom=Side(style='thick'))
print("Loading file...")
wb = load_workbook("cell.xlsx", read_only=True)
ws = wb.worksheets[0]
print("Done")

'''
A - артикул (3 merged cells)
D - наименование товара
G - адресом
J - колличество(шт)
ws.max_row - количество строк на листе
'''

raw_data = {}
print("Collecting data...")
for i in range(1, 100):
	art = ws[f"A{i}"].value
	name = ws[f"D{i}"].value
	adr = ws[f"G{i}"].value
	q = ws[f"J{i}"].value
	if adr in raw_data:
		raw_data[adr].append([name, art, q])
		print(i)
	else:
		raw_data[adr] = [[name, art, q]]
		print(i)
print("raw_data collected.")
wb.close()

adressless = {} # Wrong adress
for key in raw_data:
	if key[2:4].isdigit() == False:
		af = raw_data.pop(key)
		adressless.update({key: af})

os.mkdir(f"{d}")
os.mkdir(f"{d}/Без адреса")

for i in range(1, 21):
	os.mkdir(f"{d}/{i} ряд")

wb = Workbook()
ws = wb.active
ws.title = "Без адреса"
ws = wb.worksheets[0]
		# ws.append(key)
		# for row in af:
		# 	ws.append(row)
wb.save(f"{d}/Без адреса/00-00.xlsx")

adr_list = list(raw_data)
adr_list.sort()
print(raw_data[adr_list[0]])

# for n in range(0, len(adr_list)):
# 	i = adr_list[n]
# 	if 

# 	if len(i) == 10:
# 		row_number = i[2:4]
# 		stak_number = i[5:7]
# 		shelf_number = i[9:]
# 		stak_title  = f"{row_number}-{stak_number}"

# 		wb = Workbook()
# 		ws = wb.active
# 		ws.title = stak_title
# 		ws.merge_cells('A1:C3')
# 		ws["A1"] = stak_title
# 		ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

# 		for row in raw_data[i]:
# 			ws.append(row)

# 		'''
# 		To do: выделить данные только на один стеллаж
# 		'''
# 		wb.save(f"{d}/{int(row_number)} ряд/{row_number} - {stak_number}.xlsx")
# 	else:
				

"""To do:
* Настроить печатную форму конечного документа
	-ширина столбца
	-размер шрифта
	-наличие заглавного номера пролёта (например 2-15)
	-масштаб на листе А4

* Распаковать row_data по документам"""
# ws["A1"] = f"{row_number} ряд, {stak_number} стеллаж"


print("Done")