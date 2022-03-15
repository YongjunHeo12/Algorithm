# 회문

# 테스트 케이스 개수
T = int(input())

# 팰린드롬을 판단할 경우가 매우 많으므로 함수로 정의
def Is_pal(words, loop_len):
    word = ''
    judge = 0
    for alphabet in words:
        word += alphabet
   
    for i in range(loop_len//2):
        if(word[i] == word[-1*i-1]):
            judge += 1

    # 루프에서 비교한 것이 모두 맞을경우 judge의 값은 루프를 돈 횟수이므로 이때 팰린드롬하다고 할 수 있음        
    if(judge == loop_len//2):
        return word
    else:
        return False    

for t in range(T):
    # N행, N열, 회문길이 M
    N, M = map(int, input().split())

    words = [list(input()) for _ in range(N)]
    words_T  = list(zip(*words))

    
    double_break = False
    answer = ''

    for r in range(N):
        if double_break:
            break

        words_line = words[r]
        words_T_line = words_T[r]

        for i in range(N-M+1):
            ans1 = Is_pal(words_line[i:i+M],M)
            ans2 = Is_pal(words_T_line[i:i+M],M)
            if ans1:
                answer = ans1
                double_break = True
                break
            elif ans2:
                answer = ans2
                double_break = True
                break
    
    print("#%d %s" %(t+1, answer))
    
