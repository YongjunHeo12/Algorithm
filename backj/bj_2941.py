# Croatia_Alphabet
# 크로아티아 알파벳을 판단할 리스트 생성
Croatia_Alphabet_List = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 단어 입력받기
word = input()

for alphabet in Croatia_Alphabet_List:
    word = word.replace(alphabet, "a")
print(len(word))
