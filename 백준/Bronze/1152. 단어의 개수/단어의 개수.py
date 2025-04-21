# 앞뒤 공백이 있다면 문자열 공백 제거
a = input().strip()

if a == "":
    print(0)

else:
    n = 0
    # 공백 앞 문자가 공백이 아니면 -> 단어가 있었다는 뜻 
    for i in range(len(a)-1):
        if (a[i] != ' ' and a[i+1] == ' '):
            n += 1
    # 단어 개수 = 공백 개수 + 1
    print(n+1)