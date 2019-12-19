# 환경변수 or 게임 데이터 -> 프로그램에 영향을 미치는 고정값(임계값)을 상수로 뺌
# 향후에는 *.py 바깥쪽으로 빼서 저장(파일 or 디비 or 서버) 
# 고정값을 바깥으로 뺌

GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9

if True:
    # 절차적 프로그램 실습
    # 간단한 게임을 구현하여
    # 긴 단위의 프로그램을 작성하고, 절차적 프로그램을 이해한다
    # 머드 게임 스타일로 터미널에서 입력하면서 게임을 진행
    # 목적, 파이썬 타입, 연산, 조건, 반복, 흐름 제어 등을 프로그램을 개발하면서 심화 학습한다
    # --------------------------------------------------------------------------------------

    # step1 게임 시작하면 "Enjoy Custom Game World" 라는 문구를 출력함
    print("Enjoy Custom Game world")

    # step2 
    #   2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력
    #   2-2 사용자가 입력할 때 무제한으로 대기함(무제한)
    #   2-3 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다
    #   2-4 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력하고 대기한다
    #   2-5 20자 이내로 입력하면 gameTitle라는 변수에 게임 제목을 담고 다음 3단계로 진입한다
    while True:
        tmp = input("게임 제목을 입력하시오, 단 {}자 이내로 입력 가능합니다.\n => " .format(GAME_TITLE_LEN_MAX)).strip()
        # 스페이스 바를 몇 번 치고 엔터를 친 것도 같이 처리한다.
        if(len(tmp)==0): # not tmp도 가능
            print("정확하게 입력하세요!")
        elif(len(tmp) >= GAME_TITLE_LEN_MAX):
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.")     
        else :
            gameTitle = tmp
            break
    
    # gameTitle이 정의된 곳 -> while 안에 else안에서 정의 
    # while 밖에서도 사용이 가능하다?, 함수나 클래스 내부에서 정의된 변수가 아닌 변수들은 모두 전역변수이다
    # (어느 곳에서든지 사용이 가능하다 <- Variable Scope(범위))

    # step3
    #   3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
    #   3-2 입력에 대한 처리는 step2와 동일하다
    #   3-3 플레이어의 이름은 player_name이라는 변수에 담는다.
    while True:
        c = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n" % PLAYER_NAME_LEN_MAX).strip()
        if(len(c)==0):
            print("정확하게 입력하세요!")
        elif(len(c) >= PLAYER_NAME_LEN_MAX):
            print("%s자가 초과되었습니다."% PLAYER_NAME_LEN_MAX)    
        else:
            player_name = c
            break

    # step4
    #   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다"
    #   4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
    #   4-3 게임 난이도는 game_level 이라는 변수에 담는다.

    while True:
        d = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다\n" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            continue
        if not tmp.isnumeric():  # 뭔가는 들었다 -> 정수가 아니면 컷
            continue
        # 입력값의 정수변환
        tmp = int(tmp)
        if tmp>9 or tmp<1:    # 1-9 이외값이면 컷
            continue
        # 정상값        
        #   4-3 게임 난이도는 game_level 이라는 변수에 담는다
        game_level = tmp
        break
        
# step 5
print( '-'*20 )
print( '현재 까지 입력 상황' )
print( 'gameTitle',   gameTitle )
print( 'player_name', player_name )
print( 'game_level',  game_level )
print( '-'*20 )