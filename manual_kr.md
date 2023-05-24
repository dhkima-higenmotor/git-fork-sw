# git-fork-sw 사용방법

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

## 클론(Clone)
### 방법 1
* 메뉴 `File - Accounts - Repository`에서 보여주는 목록 중에 저장소를 고른 후 우측끝 `아래쪽 화살표` 버튼을 누르면 Clone이 됨
### 방법 2
* github.com 사이트에서 원하는 저장소의 https 주소를 복사
* git-fork에서 메뉴 `File - Clone` 선택후 OK하면 Clone이 됨

## 자동화된 신규 저장소 생성 (기구팀 데이타 저장 전용)
* 메뉴 `Repository - [PDM] Make new repo` 선택
* 팝업창이 뜨면, 원하는 저장소 이름을 써 넣고 OK
* 저장소 이름의 조건은
  1. 영문, 숫자, -, _ 으로만 구성
  2. 대소문자 구분할 것
  3. 한글 사용 금지
  4. 너무 긴 이름 사용 금지 (10자 이내 권장)
  5. 프로젝트 명칭과 일치 권장
* 잠시 기다리면 웹브라우저가 뜨고, github의 저장소 Settings 페이지가 열림
* 아래쪽으로 스크롤해서 내려가다 보면 `Archives` 항목이 나옴
* `Include Git LFS objects in archives`를 반드시 체크할 것 (필수)
* 신규 저장소 생성 자동화 과정은 아래와 같음
  1. github에 원격으로 저장소를 생성
  2. 로컬 컴퓨터로 클론 후 기본 설정 파일 자동 복사
  3. 다시 github로 푸시(push)
  4. 최종적으로 웹브라우저 Settings 페이지에서 사용자가 직접 LFS 설정을 체크해 주면 끝

## 개인 브랜치 만들기(Branch)

## main 브랜치에서 개인 브랜치로 병합

## 개인 브랜치 푸시(push)

## 모든 브랜치 한꺼번에 당겨오기(push)

## 기타 잡기능

