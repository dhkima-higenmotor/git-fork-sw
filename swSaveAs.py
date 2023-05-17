import win32com.client
import time
import sys
import os

working_path = os.getcwd()
sld_file_path = f"{working_path}\\{sys.argv[1]}"
sld_extension = os.path.splitext(sld_file_path)[1]
new_file_path =  sld_file_path.rstrip(f".{sld_extension}") + "." + sys.argv[2]

swApp = win32com.client.Dispatch('SldWorks.Application')
swApp.Visible = False
time.sleep(1)

f = swApp.getopendocspec(sld_file_path)
Model = swApp.opendoc7(f)

if os.path.exists(new_file_path):
    os.remove(new_file_path)

Result = Model.SaveAs(new_file_path)

swApp.CloseAllDocuments(True)
swApp.ExitApp()
