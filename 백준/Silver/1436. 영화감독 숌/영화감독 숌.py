n = int(input())
cnt = 1
result = 0

while True :
    cnt += 1
    # 특정 숫자 값이 666을 포함하면 카운트하기.
    if "666" in str(cnt) :
        result += 1
        if result == n :
            break
print(cnt)