# 6장의 카드를 랜덤으로 생성하기 위해 랜덤 모듈 import 
import random as rand

# 6장의 카드를 생성하기 위해 지정
card_num = 6
# 카드를 담을 리스트 
cards = []
# 받은 카드의 각 숫자가 몇 개인지 카운트 하기 위해 생성한 리스트
card_count = [0] * 10

# 카드를 주는 행동을 하는 for loop
for i in range(card_num):
    cards.append(rand.randrange(0,10)) # 0~9까지의 숫자를 랜덤으로 6개 뽑아서 cards에 append

# cards에 있는 카드의 숫자들을 card_count의 인덱스로 해서 한개씩 count
for num in cards:
    card_count[num] += 1

# Run을 판단하는 flag
is_Run = False

# index가 1부터 4인 카드만 앞뒤 숫자와 비교하면 됨
for num in range(1,4):
    if(cards[num] + 1 == cards[num+1] and cards[num] - 1 == cards[num-1]): # 뒤에 카드가 1 크고 앞에카드가 1 작으면 연속
        is_Run = True
    
# Triplet을 판단하는 flag
is_Triplet = False

# card_count내의 숫자들이 3번 카운트 된 경우 Triplet 출력(숫자가 3번 카운트 된것은 cards내의 같은 숫자가 3개가 있다는 뜻이기 떄문)
for num in card_count:
    if num >= 3:
        is_Triplet = True
        break

# 내가 받은 카드 
print("내가 받은 카드는?")
print(cards)

# 출력 조건문
if is_Triplet and is_Run:
    print("Triplet! and Run!")
elif is_Triplet:
    print("Triplet!") 
elif is_Run:
    print("Run!")
else:
    print("Nothing!")   
