# git-fork 및 git-fork-sw 사용방법

## git-fork 사용시 장점
* 시험판 사용에 법적 제약이 없음 (시험판 사용기간 제한이 없음)
* 여러개의 사용자계정으로 운용할 때도 대응 가능
* 기본 부가기능 풍부
* 커스텀 명령 추가 가능

## Github 계정 등록
* 메뉴 `File - Accounts` 에서 관리
* 좌측하단 `+`, `-` 버튼으로 계정 등록, 삭제 가능
* https 프로토콜에서, 복수의 Github 계정 관리도 가능함 (git-fork 자체 관리)
* `+` 버튼을 눌러서 신규 계정 등록 시작
* `Github - Login` 선택
* `Personal Access Token` 으로 변경하고, Token 값을 복사해서 넣은 후 `Sign In` 버튼 눌러서 완료
* 최초 접속시 Github.com 웹페이지가 열리면서 `mech-higenmotor` 조직도 보여지게 할 것인지 확인하는 버튼이 나오는데, 반드시 눌러줄 것
* 우측섹터에서 `Repository` 탭을 선택후, 인식되는 저장소 목록을 확인
* `mech-higenmotor` 저장소들이 나타나는지 확인


## 1. [PM] 신규 저장소 생성

*기구팀용 신규 저장소 생성 자동화*

* 신규 프로젝트 진행시 생성
* 메뉴 `Repository - [PDM] Make new repo` 선택
* 팝업창이 뜨면, 원하는 저장소 이름을 써 넣고 OK
> 저장소 이름은 가능한 알파벳,숫자,대쉬기호만으로 만드는 것이 좋겠고, 그 이름을 프로젝트 명칭으로 삼는 것이 유리함
* 잠시 기다리면 웹브라우저가 뜨고, github의 저장소 Settings 페이지가 열림
* 아래쪽으로 스크롤해서 내려가다 보면 `Archives` 항목이 나옴
* `Include Git LFS objects in archives`를 반드시 체크할 것 (필수)


## 2. [팀원] 클론(Clone)

*리모트 저장소를 로컬로 처음 가져오기*

### 방법 1
* 메뉴 `File - Accounts - Repository`에서 보여주는 목록 중에 저장소를 고른 후 우측끝 `아래쪽 화살표` 버튼을 누르면 Clone이 됨
### 방법 2
* github.com 사이트에서 원하는 저장소의 https 주소를 복사
* git-fork에서 메뉴 `File - Clone` 선택후 OK하면 Clone이 됨
* 이때 복수의 사용자계정을 운용할 경우, 사용자계정 확인후 정확히 선택할 것


## 3. 모든 브랜치 한꺼번에 당겨오기(push)

*로컬 저장소 최신 업데이트*

* 메뉴 `Repository` - `[PDM] PULL all branches` 를 선택하여 모든 브랜치를 한꺼번에 로컬로 업데이트


## 4. [팀원] 작업용 브랜치 만들기(Branch)

*브랜치를 만들어서 작업한 후, PM에게 병합요청(Pull Request)*

* 좌측영역의 `Branches`의 컨텍스트 메뉴에 `New Branch`를 선택해서 신규 브랜치 생성
* 브랜치 이름은 자신의 사용자계정 이름을 사용
* `Checkout after create`를 체크해 주면, 만들어진 브랜치에 자동적으로 들어감(Checkout)


## 5. [팀원] 브랜치 이동 및 main 병합후 솔리드웍스 작업 실시

### 브랜치 이동
* 이미 만들어진 브랜치로 이동할 때는 해당 브랜치를 더블클릭
* 작업용 브랜치에 체크아웃후, 작업시작전 main 브랜치를 병합해서 업데이트해 줄 것
### 병합방법 1
* main 브랜치의 컨텍스트 메뉴에서 `Merge into <현재브랜치>`를 선택
* 충돌(Conflict)가 발생하면, 지시에 따라 우선권이 있는 파일을 선택하고 좌측하단의 `commit` 버튼을 눌러주면 됨
### 병합방법 2
* main 브랜치의 컨텍스트 메뉴에서 `[PDM] MERGE force into current branch`를 선택
* 충돌 여부를 따지지 않고 무조건 main 브랜치 우선으로 덮어써서 병합함
### 작업실시
* 메뉴 `Repository` - `[PDM] SW start` 를 선택하면 솔리드웍스 시작


## 6. [팀원] 솔리드웍스 작업 완료후 작업 브랜치 푸시(push)
* 솔리드웍스 작업이 완료되었으면, 리모트로 푸시해야 함
* 좌측상단부 `Local Changes`를 선택하면 `Unstaged` 파일 목록이 나타남
* 업데이트 대상파일들을 모두 선택후 `Stage` 버튼 누르면 `Staged` 영역으로 이동함
* 우측하단의 `Commit Subject` 칸에 커밋 메시지를 써줌
> 간단히 마일스톤,버전번호 또는 변경사항을 메모해 주면 됨
* 맨 우측하단의 `Commit`버튼을 눌러서 커밋함
* 맨 좌측상단의 `Push` 아이콘 버튼을 눌러서 리모트로 푸시


## 7. [PM] 팀원의 작업 브랜치를 main 브랜치로 병합후 푸시
* 로컬 저장소 업데이트 (3번 방법)
* main 브랜치를 더블클릭하여 이동
* 병합을 원하는 팀원의 작업 브랜치의 컨텍스트 메뉴를 병합 (상기 5번의 병합방법 1,2)
* 병합이 끝났으면 푸시 (6번 방법)


## 파일 관련 잡기능

### 파일 찾기 용이한 모드로 전환
* 좌측 상단의 `All Commits`를 선택하면 커밋 히스토리 모드로 전환된다.
* 하단영역의 탭(`Commit`, `Changes`, `File Tree`) 중에서 `File Tree`를 선택
* 상단영역의 커밋 히스토리 중에서 원하는 커밋을 선택하면, 선택된 커밋의 `File Tree`를 볼 수 있음

### 내장 diff
* 변경사항을 비교해서 보여주는 기능임
* git-fork는 텍스트파일, 그림파일에 대한 diff 기능이 내장되어 있음
* 하단영역의 탭(`Commit`, `Changes`, `File Tree`) 중에서 `Changes`를 선택하고 원하는 파일을 선택하면 됨

### 커스텀 diff
* pdf, png 파일을 직전 커밋 버전과 비교해서 보여주는 기능 추가
* 커밋 히스토리 중에서, 원하는 커밋을 더블클릭하여 들어감(Checkout)
* `File Tree`에서 원하는 파일 선택 (확장자 PDF, PNG일 것)
* 원하는 파일의 컨텍스트 메뉴에서 `[PDM] diff binary` 중에서 `PDF`, `PNG` 중 선택

### 솔리드웍스 파일 출력
* 해당파일을 솔리드웍스로 열어서 PDF,DXF,STEP,BOM(csv) 파일로 변환해서 출력
* 커밋 히스토리 중에서, 원하는 커밋을 더블클릭하여 들어감(Checkout)
* `File Tree`에서 원하는 파일 선택 (확장자 SLDPRT,SLDASM,DXF일 것)
* 원하는 파일의 컨텍스트 메뉴에서 `[PDM] SW export` 중에서 원하는 기능 선택
* 솔리드웍스가 열려있는 상태일 경우에는 빠르게 진행되지만, 열려있지 않을 경우에는 백그라운드에서 느리게 열려서 진행됨
* 솔리드웍스가 백그라운드에서 열렸을 경우 자동으로 닫히지 않으므로, `Repository` - `[PDM] SW taskkill`으로 강제로 종료하면 됨
* 변환된 파일들은 `2D/` 디렉토리에 저장되며, 버전관리에서는 무시됨

### 솔리드웍스 파일 보기
* 해당파일을 열어서 eDrawing로 보기
* 커밋 히스토리 중에서, 원하는 커밋을 더블클릭하여 들어감(Checkout)
* `File Tree`에서 원하는 파일 선택 (확장자 SLDPRT,SLDASM일 것)
* 원하는 파일의 컨텍스트 메뉴에서 `[PDM] View` 중에서 원하는 기능 선택
* BOM(csv) 보기의 경우에는, `BOM/` 디렉토리에 저장되며, 버전관리에서는 무시됨

