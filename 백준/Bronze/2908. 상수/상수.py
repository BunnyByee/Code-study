a, b = input().split()

# 문자열 뒤집고 숫자로 변환해서 비교
if (int(a[::-1]) > int(b[::-1])) :
    print(a[::-1])
else :
    print(b[::-1])