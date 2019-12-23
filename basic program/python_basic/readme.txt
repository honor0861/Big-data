WIFI : hgr8083700

출결 중요 (입실, 퇴실 체크)
자료실 => http://192.168.0.119/

2020년 9월 빅데이터 기사 제1회(확인 필요)

6시간(수업) / 2시간(자율)
kaggle => 외국 빅데이터 분석 대회

12.26일 회식(예정)
---------------------------------------
전체과정
1. 개요
- Python을 기반
- 데이터 분석(통계적, 시각적), 수집 전 처리 등
- 머신러닝, 딥러닝(그래픽카드 사용) => AI분야
	-> NVIDIA(CUPA가 Window와 Linux 지원 cf. Mac은 배제함) vs AMD
- 빅데이터 처리 => 하둡 클러스터 관련 시스템
- 파이널 프로젝트

2. 개발 환경
- OS : Window, MAC, Linux
- python : 
	- 버전
	  - 2.7 <- MAC 기본설치 버전, 리눅스 기본설치 버전
	  - 3.x : 개발(3.7 or 3.6) * 최신버전이 좋은 건 아님
	- 설치 
	  - python.org(파이썬만 깔림)
 	    if. 현재 PC에 3.7 깔았을 경우 -> 3.5 필요하다? => 지우고 다시 재설치해야 하는 번거로움
	- 한 PC에서 여러 버전 사용할 수 있다면 
	   -> 가상환경을 구축해서 각각 영향을 주지 않고 사용
	   -> 요구사항을 간편히 수행할 수 있는 Full Package Installer => *** "Anaconda" 설치! ***
	   -> https://www.anaconda.com/ 
	   -> 아나콘다의 라이트버전(커맨드 버전)
- IDE : 개발 통합 환경
        => 전용툴 : Python IDE(사용할 일 X), 파이참(시스템이 안 받쳐주면 느림)
	           , 파이데브, 스파이더, Jupiter notebook(분석툴, 머신러닝, 딥러닝에 사용됨=> 브라우저에서 코딩(웹 기반))
	           , L ipython(커맨드 스타일 분석툴) + 웹 환경(Flask)
        => 범용툴 : 기존의 개발환경 + 플러그인 추가
	            vs Code + python + anaconda + jupiter
- 공정관리
	 - "github.com" (회원가입 및 대학생이면 인증(차후)
	   - 대학생 혜택(private 기능 무료 사용)
	     https://limetimeline.tistory.com/277
	 - 개발 PC에 git에 설치 "https://git-scm.com/download/win"

3. 설치
- anaconda -> git -> vs code 순으로 설치(순서는 상관없음)
  아나콘다 경로 : C:\Users\admin\Anaconda3
  git - Use Visual Studio Code as Git's default editor(위에서 4번째)

4. VS Code 설정
- 프로젝트를 원하는 위치에 폴더 생성(python_projects라고 폴더이름 생성)
  - 해당 폴더를 드래그, VS Code에 드롭
  - 해당 위치로 VS Code 재오픈
- Editor 설정
  - File > preferences > settings
  - 검색(Indexing) > 항목을 찾아서 수정
  - Thema > Color Theme > Default Light + 
    font에서 수치조정 가능
    전체 줌 "Ctrl +" or "Ctrl -"
 - 왼쪽 메뉴
	- file Explorer
	- 검색, 대체
	- 공정관리 : 소스 컨트롤
	- 디버깅(코드 오류가 있을 때 잡는 방법)
	- 플러그인 검색 및 설치
 - Python 설치 이후 Python 파일 한 개를 생성하면
    -./basic/p1.py
	- vs code가 해당 파일을 인식하고, python 경로를 잡거나 extention을 설치하라고 유도
	  -> vs code 재가동
	  -> 왼쪽 메뉴 5번째 extention 항목에서 python 검색(python, python for vs code, python extention pack) 설치