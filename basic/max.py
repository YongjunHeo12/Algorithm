# max값을 찾을 리스트
nums = [1, 5 ,77, 26, 33, 2, 6, 16, 55]
# 초기 max를 0으로 설정
max_num = 0
# loop를 통해 max 찾기
for num in nums:
    if num > max_num:
        max_num = num
print(max_num)