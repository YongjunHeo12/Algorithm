# min max

# 테스트 케이스 개수
T = int(input())

# N개의 양수
for i in range(T):
    # 각 케이스의 양수의 개수
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = max(numbers)-min(numbers)
    print("#%d %d"  %(i+1,ans))