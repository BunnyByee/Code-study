n = int(input())

for _ in range(n):
    # 횟수, 문자열 입력
    a, b = input().split()

    for s in b: # 문자*a 개 출력
        print(s*int(a), end='')
    print()