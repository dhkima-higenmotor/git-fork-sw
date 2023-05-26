
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

# Path for eDrawings like that :
reg add "HKCU\Environment" /v path /t REG_EXPAND_SZ /d "%path%;C:\Program Files\SOLIDWORKS Corp\eDrawings" /f

# Refresh env variables
taskkill /f /im explorer.exe
explorer.exe
```
