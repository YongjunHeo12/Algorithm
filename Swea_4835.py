# 구간합

# 테스트케이스 개수 
T = int(input())

for t in range(T):
    # 각 줄의 정수의 개수와 구간의 개수 입력받기
    N, M = map(int,input().split())

    # 정수 N개 입력받기
    Numbers = list(map(int,input().split()))
    
    # 구간합을 임시로 저장할 리스트
    Prefix_sum = []
    
    for i in range(N-M+1):
        total = 0
        for n in range(M):
            total = total + Numbers[i+n]
        Prefix_sum.append(total)

    print("#%d %d" %(t+1, max(Prefix_sum)-min(Prefix_sum)))

