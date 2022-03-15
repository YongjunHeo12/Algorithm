# 구슬치기 

# 테스트 케이스 숫자
T = int(input())

# 테스트 케이스 만큼 숫자 입력받기
for i in range(T):
    
    Participant_list = list(map(int, input().split()))
    
    count_dict = dict()
    
    for num in Participant_list:
        if not count_dict.get(num):
            count_dict[num] = 1
        else:
            count_dict[num] += 1
  
    for key, value in count_dict.items():
        if value == 1:   
            print("#%d %d" %(i+1, key))
            break