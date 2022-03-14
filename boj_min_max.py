# 정수의 개수 입력받기
num_len = map(int, input())

# 리스트에 들어갈 숫자 입력받기
num_list = list(map(int, input().split()))

# max, min 이용하여 최대 최소 구하기
max_num = max(num_list)
min_num = min(num_list)

print("%d %d" %(min_num, max_num))