import PySimpleGUI as sg
import csv
import os
import sys

# paths
sld_file_path = sys.argv[1]
sld_basename = os.path.basename(sld_file_path)
sld_basename = os.path.splitext(sld_basename)[0]
sld_extension = os.path.splitext(sld_file_path)[1]
working_path = os.path.dirname(sld_file_path)
BOM_path = f"{working_path}\\BOM"
csv_file_path = f"{BOM_path}\\{sld_basename}.csv"

def readBOM():
    data = list()
    if os.path.isfile(csv_file_path):
        f = open(csv_file_path,'r')
        rea = csv.reader(f)
        for row in rea:
            data.append(row)
        f.close
    return data

# Table GUI
sg.set_options(font=("D2Coding",12))
BOM = readBOM()
if not BOM:
    sg.popup(f"Not exist {csv_file_path}")
    sys.exit()

toprow = ['0','1','2','3','4','5','6','7','8','9']
tbl1 = sg.Table(values=BOM,
    headings=toprow,
    auto_size_columns=True,
    display_row_numbers=True,
    justification='left', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

layout = [[tbl1],
          [sg.Button('CLICK',key='-CLICK-'), sg.Button('EXIT',key='-EXIT-')]]
window = sg.Window("BOM Table", layout, size=(800,600), resizable=True)

while True:
    event, values = window.read()
    print("event:", event, "values:", values)
    if event in (sg.WIN_CLOSED, "-EXIT-"):
        break
    elif '+CLICKED+' in event:
        pass
    elif event=='-CLICK-':
        sg.popup(f"{values['-TABLE-']}")

window.close()