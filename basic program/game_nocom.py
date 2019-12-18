print("Enjoy World")
while True:
    tmp = input("게임 제목 입력, 단 20자 이내 입력\n").strip()
    if not tmp:
        print("정확하게 입력하세요")
    elif(len(tmp)>= 20):
        print("20자가 초과되었습니다")
    else:
        gameTitle = tmp
        break
print('gameTitle : ',gameTitle)

while True:
    tmp = input("플레이어의 닉네임을 입력하시오, 단 15자로 제한한다")
    if not tmp:
        print("정확하게 입력하세요")
    elif(len(tmp)>= 15):
        print("15자가 초과되었습니다")
    else:
        player_name = tmp
        break
print('player_name : ', player_name)

