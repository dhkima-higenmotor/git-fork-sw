import os
import sys
import win32com.client

# Repo Directory
REPO_DIR = sys.argv[1]

# Change into Repo Directory
os.chdir(REPO_DIR)

# Lists
def LISTING(filename):
    f = open(filename, 'r')
    TEMP1 = f.readlines()
    f.close()
    TEMP2 = [l.strip() for l in TEMP1]
    TEMP3 = []
    for line in TEMP2:
        if ('~' not in line) and ('_SKEL' not in line) and ('TOTAL_LIST_TEMP.CSV' not in line) and ('MOD_LIST_TEMP.CSV' not in line) and ('.SLDASM' not in line) and ('/2D/' not in line):
            if ('.SLDPRT' in line) or ('.SLDDRW' in line):
                TEMP3.append(line)
    return TEMP3

CACHED_LIST_TEMP = LISTING("CACHED_LIST.CSV")
DELETED_LIST_TEMP = LISTING("DELETED_LIST.CSV")
MODIFIED_LIST_TEMP = LISTING("MODIFIED_LIST.CSV")
OTHERS_LIST_TEMP = LISTING("OTHERS_LIST.CSV")

# Modify Lists
def LISTING2(list):
    list2 = []
    for line in list:
        if ('~' not in line) and ('_SKEL' not in line) and ('.CSV' not in line) and ('.gitattributes' not in line) and ('.md' not in line) and ('.gitignore' not in line) and ('.SLDASM' not in line) and ('/2D' not in line):
            if ('.SLDPRT' in line) or ('.SLDDRW' in line):
                list2.append(line)
    return list2

CACHED_LIST = LISTING2(CACHED_LIST_TEMP)
DELETED_LIST = LISTING2(DELETED_LIST_TEMP)
MODIFIED_LIST = LISTING2(MODIFIED_LIST_TEMP)
OTHERS_LIST = LISTING2(OTHERS_LIST_TEMP)

# Generating New List
CACHED_SET = set(CACHED_LIST)
MODIFIED_SET = set(MODIFIED_LIST)
OTHERS_SET = set(OTHERS_LIST)
NEW_LIST = list(CACHED_SET-MODIFIED_SET)

# Devide Lists
def DEVIDE(list_temp):
    LIST = []
    for line3 in list_temp:
        # Directory
        FILE_DIR_TEMP = os.path.dirname(line3)
        FILE_DIR = REPO_DIR.replace("/","\\") + "\\" + FILE_DIR_TEMP.replace("/","\\")
        # Basename
        FILE_BASENAME_TEMP = os.path.basename(line3)
        FILE_BASENAME = os.path.splitext(FILE_BASENAME_TEMP)[0]
        # Extension
        FILE_EXTENSIONE = os.path.splitext(FILE_BASENAME_TEMP)[1]
        LIST.append([FILE_DIR,FILE_BASENAME,FILE_EXTENSIONE])
    return LIST

CACHED = DEVIDE(CACHED_LIST)
DELETED = DEVIDE(DELETED_LIST)
MODIFIED = DEVIDE(MODIFIED_LIST)
OTHERS = DEVIDE(OTHERS_LIST)
NEW = DEVIDE(NEW_LIST)

# Delete old DXF,PDF,STEP
def DELETE(dir, basename, extension):
    if DELETED_LIST != []:
        for dir, basename, extension in DELETED:
            if extension == ".SLDDRW":
                PDF_TEMP = f"{dir}\\2D\\PDF\\{basename}.PDF"
                DXF_TEMP = f"{dir}\\2D\\DXF\\{basename}.DXF"
                if os.path.isfile(PDF_TEMP):
                    os.remove(PDF_TEMP)
                if os.path.isfile(DXF_TEMP):
                    os.remove(DXF_TEMP)
            if extension == ".SLDPRT":
                STEP_TEMP = f"{dir}\\2D\\STEP\\{basename}.STEP"
                if os.path.isfile(STEP_TEMP):
                    os.remove(STEP_TEMP)

for line in DELETED:
    DELETE(line[0],line[1],line[2])

for line in MODIFIED:
    DELETE(line[0],line[1],line[2])

# Generate Exports
def GENERATE(dir, basename, extension, flag):
    TOTAL_PATH = f"{dir}\\{basename}{extension}"
    STEP_TEMP = f"{dir}\\2D\\STEP\\{basename}.STEP"
    PDF_TEMP = f"{dir}\\2D\\PDF\\{basename}.PDF"
    DXF_TEMP = f"{dir}\\2D\\DXF\\{basename}.DXF"
    if not os.path.isdir(f"{dir}\\2D"):
        os.makedirs(f"{dir}\\2D")
    swApp = win32com.client.Dispatch('SldWorks.Application')
    if basename != None:
        if (extension == ".SLDPRT") and (os.path.isfile(STEP_TEMP)):
            flag2 = 0
        else:
            flag2 = 1
        if (extension == ".SLDDRW") and (os.path.isfile(PDF_TEMP) and os.path.isfile(DXF_TEMP)):
            flag2 = 0
        else:
            flag2 = 1
        if ((flag == "MODIFIED") or (flag == "NEW")) and (flag2 == 1):
            f = swApp.getopendocspec(TOTAL_PATH)
            Model = swApp.opendoc7(f)
            if extension == ".SLDPRT":
                if not os.path.isdir(f"{dir}\\2D\\STEP"):
                    os.makedirs(f"{dir}\\2D\\STEP")
                Model.SaveAs(STEP_TEMP)
                print(f"{os.path.isfile(STEP_TEMP)} : {STEP_TEMP}")
            elif extension == ".SLDDRW":
                if not os.path.isdir(f"{dir}\\2D\\PDF"):
                    os.makedirs(f"{dir}\\2D\\PDF")
                if not os.path.isdir(f"{dir}\\2D\\DXF"):
                    os.makedirs(f"{dir}\\2D\\DXF")
                Model.SaveAs(PDF_TEMP)
                Model.SaveAs(DXF_TEMP)
                print(f"{os.path.isfile(PDF_TEMP)} : {PDF_TEMP}")
                print(f"{os.path.isfile(DXF_TEMP)} : {DXF_TEMP}")
            swApp.CloseDoc(TOTAL_PATH)

for line in MODIFIED:
    GENERATE(line[0],line[1],line[2],"MODIFIED")

for line in NEW:
    GENERATE(line[0],line[1],line[2],"NEW")

print("Finished.")
