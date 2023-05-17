

## 설치해야 하는 소프트웨어

* scoop

```powershell
powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
irm get.scoop.sh | iex
```

* git-fork
  - `%userprofile%\AppData\Local\Fork\Fork.exe`f

* ImageMagick
  - Recommend : `scoop install diff-pdf` : Not absolute

* 꿀뷰(Honeyview)
  - `C:\Program Files\Honeyview\Honeyview.exe`

* Python3 (Recommended Miniconda3)
  - `conda install pywin32` : Not absolute

* diff-pdf
  - Recommend : `scoop install diff-pdf` : Not absolute

* SumatraPDF
  - `C:\Program Files\SumatraPDF\SumatraPDF.exe`

* Solidworks 2023
  - `C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\SLDWORKS.exe` : Not absolute


## git-fork-sw 설치

```
bash
git clone https://github.com/dhkima-higenmotor/git-fork-sw.git /d/github/git-fork-sw
cp /d/github/git-fork-sw/custom-commands.json %HOME/AppData/Local/Fork/custom-commands.json
```

* 설치 소프트웨어 경로가 다를 경우 `custom-commands.json` 내용 편집할 것


## Custom Commands

### PULL : 모든 브랜치 한꺼번에
* Repository 메뉴에 뜸
* 모든 원격브랜치를 싹 다 가져옴


### MERGE : 현재 브랜치로 강제병합
* Branch 컨텍스트 메뉴에 뜸
* 선택한 브랜치를 현재 브랜치로 강제로 덮어씀

### PULL : 현재 및 main 브랜치
* Branch 컨텍스트 메뉴에 뜸
* 현재 브랜치, main 브랜치만 가져옴


### diff PDF
* File 컨텍스트 메뉴에 뜸
* HEAD, HEAD^ 비교파일을 임시로 생성후 보여줌

### diff PNG
* File 컨텍스트 메뉴에 뜸
* HEAD, HEAD^ 비교파일을 임시로 생성후 보여줌

### SLDDRW > DXF
* File 컨텍스트 메뉴에 뜸
* 솔리드웍스 도면파일을 DXF로 출력

### SLDDRW > PDF
* File 컨텍스트 메뉴에 뜸
* 솔리드웍스 도면파일을 PDF로 출력

### SLDPRT,SLDASM > STEP
* File 컨텍스트 메뉴에 뜸
* 솔리드웍스 파트, 어셈블리 파일을 STEP으로 출력


