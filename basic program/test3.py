# 트럼프 카드 준비
seq = list('♠◆♥♣')
nums = list('A23456789') + ['10'] + list('JQK')
cards = [i+j for i in seq for j in nums]
# 셔플
import random
random.shuffle(cards)
print(cards[:8])
print('나의 카드', cards[:8:2])
print('컴퓨터의 카드', cards[1:9:2])
# 카드 합산
# 내 카드 합산 : 최초 2개
my_first_card = cards[:8:2][:2]
print(my_first_card)
# -> 정수값 추출 : 멤버 하나 추출 -> 슬라이싱 or 추출 or 분해

sum = 0
for n in my_first_card:
    # 타입을 제거(0번째 문자)
    tmp = n[1:]
    if tmp == 'A' or tmp == 'J' or tmp =='Q' or tmp == 'K':
        # -> 합하기
        if tmp == 'A': sum += 1
        elif tmp == 'J': sum += 11
        elif tmp == 'Q': sum += 12
        elif tmp == 'K': sum += 13
    else: # 기본형이 정수
        # sum += int(tmp)
        sum = sum + int(tmp)

#################################################
# A~K까지를 키로 보고, 이를 통해 값을 획득하면 간단하게 합산
# 이를 위해 점수 변환표를 준비함

score_table = dict()
for key in nums:
    # 1~13값을 차례대로 넣어라
    score_table[key] = nums.index(key) + 1
print(score_table)

score_table = dict()
k = 1 
for key in nums:
    score_table[key] = k
    k += 1
print(score_table)

# 합산값
sum = 0
for n in my_first_card:
    sum += score_table[n[1:]]
print(n[1:])
print(score_table[n[1:]])
print('내 최초 카드 2장의 합', sum)
'''
computer_first_card = cards[1:9:2][:2]
print(computer_first_card)

for m in computer_first_card:
    tmp = m[1:]
    if tmp == 'A' or tmp == 'J' or tmp =='Q' or tmp == 'K':
        # -> 합하기
        if tmp == 'A': sum += 1
        elif tmp == 'J': sum += 11
        elif tmp == 'Q': sum += 12
        elif tmp == 'K': sum += 13
    else:
        print(int(tmp))

'''