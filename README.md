
# git-for-sw

**Custom Commands for git-fork to Simple Solidworks PDM**


## Abstract

* Using git-fork as a Simple PDM
* [Simple User Manual in Korean](manual_kr.md)


## Must be installed

* [MyScoop](https://github.com/dymaxionkim/MyScoop) toolchain
* [git-fork](https://git-fork.com/)
* [Solidworks](https://www.solidworks.com/ko)
* [eDrawings](https://www.edrawingsviewer.com/download-edrawings)


## git-fork-sw

```cmd
git clone https://github.com/dhkima-higenmotor/git-fork-sw.git D:\github\git-fork-sw
copy D:\github\git-fork-sw\custom-commands.json %userprofile%\AppData\Local\Fork\custom-commands.json
```

```cmd
# find eDrawings.exe
es eDrawings.exe
# Path for eDrawings
reg add "HKCU\Environment" /v path /t REG_EXPAND_SZ /d "%path%;C:\Program Files\SOLIDWORKS Corp\eDrawings" /f
# Refresh env variables
taskkill /f /im explorer.exe
explorer.exe
```


## Custom Commands

### [PDM] View / [eDrawings] 2D,3D View
* File Context Menu
* Need : eDrawings viewer or eDrawings Professional
* View Solidworks File, STEP, IGES, STL

### [PDM] View / BOM (csv)
* File Context Menu
* Need : Solidworks
* View BOM Tree from .SLDASM file

### [PDM] SW Export / SLDDRW > DXF
* File Context Menu
* Need : Solidworks
* Export dxf drawing file

### [PDM] SW Export / SLDDRW > PDF
* File Context Menu
* Need : Solidworks
* Export pdf drawing file

### [PDM] SW Export / SLDPRT,SLDASM > STEP
* File Context Menu
* Need : Solidworks
* Export STEP file

### [PDM] SW Export / SLDASM > BOM (csv)
* File Context Menu
* Need : Solidworks
* Export csv BOM Tree file from .SLDASM file

### [PDM] diff binary / PDF
* File Context Menu
* Need : ImageMagick, mupdf
* Compare current and previous version

### [PDM] diff binary / PNG
* File Context Menu
* Need : ImageMagick, qView
* Compare current and previous version

### [PDM] MERGE force into current branch
* Branch Context Menu
* git merge -Xtheir

### [PDM] PULL main and current branch
* Branch Context Menu
* git pull main and current branch

### [PDM] PULL all branches
* Repository Menu
* git pull --all

