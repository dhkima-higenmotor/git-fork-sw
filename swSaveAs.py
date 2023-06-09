import win32com.client
import time
import sys
import os

sld_file_path = sys.argv[1]
sld_basename = os.path.basename(sld_file_path)
sld_basename = os.path.splitext(sld_basename)[0]
sld_extension = os.path.splitext(sld_file_path)[1]
working_path = os.path.dirname(sld_file_path)
DRAWING_path = f"{working_path}\\2D"
TARGET = f"{sys.argv[2]}"

if not os.path.isdir(DRAWING_path):
    os.mkdir(DRAWING_path)
if not os.path.isdir(f"{DRAWING_path}\\{TARGET}"):
    os.mkdir(f"{DRAWING_path}\\{TARGET}")
if TARGET == "STEP":
    new_file_path = f"{DRAWING_path}\\STEP\\{sld_basename}.{TARGET}"
elif TARGET == "DXF":
    new_file_path = f"{DRAWING_path}\\DXF\\{sld_basename}.{TARGET}"
elif TARGET == "DWG":
    new_file_path = f"{DRAWING_path}\\DWG\\{sld_basename}.{TARGET}"
elif TARGET == "PDF":
    new_file_path = f"{DRAWING_path}\\PDF\\{sld_basename}.{TARGET}"
else:
    new_file_path = f"{DRAWING_path}\\{sld_basename}.{TARGET}"

swApp = win32com.client.Dispatch('SldWorks.Application')
swApp.Visible = False
time.sleep(1)

f = swApp.getopendocspec(sld_file_path)
Model = swApp.opendoc7(f)

Result = Model.SaveAs(new_file_path)

swApp.CloseDoc(sld_file_path)
#swApp.CloseAllDocuments(True)
#swApp.ExitApp()
print(new_file_path)