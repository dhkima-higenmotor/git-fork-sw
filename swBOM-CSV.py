import win32com.client
import sys
import os
import re
import csv

# paths
#working_path = os.getcwd()
#sld_file_path = f"{working_path}\\{sys.argv[1]}"
sld_file_path = sys.argv[1]
sld_basename = os.path.basename(sld_file_path)
sld_basename = os.path.splitext(sld_basename)[0]
sld_extension = os.path.splitext(sld_file_path)[1]
working_path = os.path.dirname(sld_file_path)
BOM_path = f"{working_path}\\BOM"
csv_file_path = f"{BOM_path}\\{sld_basename}.csv"

# BOM List
list_component = []
row = 1
def listComponent(component):
    global row
    comp1 = component.Name2
    comp1 = re.sub(r'-[0-9]*','',comp1)
    comp2 = comp1.split('/')
    list_component.append(comp2)
    row += 1
    for child in component.GetChildren:
        listComponent(child)

# Open Doc
swApp = win32com.client.Dispatch("SldWorks.Application")
f = swApp.getopendocspec(sld_file_path)
assembly = swApp.opendoc7(f)

# Get the assembly tree root component
rootComponent = assembly.GetActiveConfiguration.GetRootComponent3(True)

# Listing
listComponent(rootComponent)

#print(list_component)
# Close SW
#swApp.ExitApp()
swApp.CloseDoc(sld_file_path)

# Save csv
if not os.path.isdir(BOM_path):
    os.mkdir(BOM_path)
with open(csv_file_path, 'w', newline='') as f:
    write = csv.writer(f) 
    write.writerows(list_component)
