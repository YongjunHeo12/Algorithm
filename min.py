# min값을 찾을 리스트
nums = [1, 5 ,77, 26, 33, 2, 6, 16, 55]
# 매우 큰 수
min_num = 99999
# loop를 통한 min값 찾기
for num in nums:
    if num < min_num:
        min_num = num
print(min_num)