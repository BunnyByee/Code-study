n = int(input())
cnt = 0

while n >= 0 :
    # 5kg로 먼저 나누기
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    # 안 나눠지면 3kg 뺴기
    n -= 3
    cnt += 1
else:  # 반복문 정상 종료 -> 나누기 실패했다는 뜻!
    print(-1)