# 세로 읽기
# 글자들을 입력받기
# 2차원 배열의 높이가 5임
words= []
for i in range(5):
    words.append(list(input()))

max_len = 0
for i in range(5):
    if max_len < len(words[i]):
        max_len = len(words[i])

ans = []

# 열 우선 순회
for r in range(max_len):
    for c in range(len(words)):
        try:
            ans.append(words[c][r])
        except:
            continue

ans_string = ''.join(ans)
print(ans_string)