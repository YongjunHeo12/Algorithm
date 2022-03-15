# study_abroad_ban(유학금지)
# 금지되는 알파벳
BAN_WORD = "CAMBRIDGE"

# 알파벳 대문자로 이루어진 단어가 주어짐
word_list = list(input())
# 주어진 단어 중 제거할 알파벳들을 저장한 리스트
remove_list = []

# 주어진 단어에서 금지된 알파벳들을 분류
for alphabet in word_list:
    for BAN in BAN_WORD: 
        if(alphabet == BAN):
            remove_list.append(alphabet)

# word_list - remove_list를 구현 
word_list = [x for x in word_list if x not in remove_list]

# 출력값은 단어이기 때문에 리스트를 스트링으로 변환
word = ''.join(word_list)

print(word)


