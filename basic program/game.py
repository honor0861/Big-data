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
    tmp = input("게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다.\n").strip()
    # 스페이스 바를 몇 번 치고 엔터를 친 것도 같이 처리한다.
    if(len(tmp)==0): # not tmp도 가능
        print("정확하게 입력하세요!")
        print()
        continue
    elif(len(tmp) >= 20):
        print("20자가 초과되었습니다.")
        print()
        continue      
    else :
        gameTitle = tmp
        break
print('gameTitle : ', gameTitle)
# step3
# gameTitle이 정의된 곳 -> while 안에 else안에서 정의 
# while 밖에서도 사용이 가능하다?, 함수나 클래스 내부에서 정의된 변수가 아닌 변수들은 모두 전역변수이다
# (어느 곳에서든지 사용이 가능하다 <- Variable Scope(범위))
#   3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
#   3-2 입력에 대한 처리는 step2와 동일하다
#   3-3 플레이어의 이름은 player_name이라는 변수에 담는다.
while True:
    c = input("플레이어의 닉네임을 입력하시오, 단 15자로 제한한다\n").strip()
    if(len(c)==0):
        print("정확하게 입력하세요!")
        print()
        continue
    elif(len(c) >= 20):
        print("20자가 초과되었습니다.")
        print()
        continue      
    else:
        player_name = c
        break
print('Player Name : ', player_name)
# step4
#   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다"
#   4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
#   4-3 게임 난이도는 game_level 이라는 변수에 담는다.

while True:
    d = input("게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다\n").strip()
    if(tmp.isalnum()):
        tmp = int(d)
        print(type(tmp))
        if(tmp > 0 & tmp < 10):
            game_level = tmp
            break
    else:
        print("Error")
        