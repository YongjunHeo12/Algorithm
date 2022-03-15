# palindrome(팰린드롬인지 확인하기)
# 팰린드롬을 확인할 단어 입력받기
word = input()

# 단어의 길이의 반의 몫 만큼 루프
loop_len =  len(word)//2

# 팰린드롬, 판단 변수 생성
is_palindrome = 0
judge = 0

# 각 단어의 처음과 끝, 2번째와 끝에서 두번째 ... 를 각각 같은지 비교
for i in range(loop_len):
    if(word[i] == word[-1*i-1]):
        judge += 1

# 루프에서 비교한 것이 모두 맞을경우 judge의 값은 루프를 돈 횟수이므로 이때 팰린드롬하다고 할 수 있음        
if(judge == loop_len):
    is_palindrome=1

print(is_palindrome)
