# odd값을 찾을 리스트
nums = [1, 5 ,77, 26, 33, 2, 6, 16, 55]

# odd값을 저장할 리스트
odd_nums = []
# loop를 통해 %2 로 짝수 걸러내기
for num in nums:
    if num % 2 != 0:
        odd_nums.append(num)

print(odd_nums)  