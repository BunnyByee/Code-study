import sys
input = sys.stdin.readline

# n개를 입력 받고, count 배열 생성
n = int(input())
C = [0] * 10001

# 입력 받는 동시에 count 해서 배열에 저장
for _ in range(n):
    num = int(input())
    C[num] += 1

# 숫자 1부터 ~ n까지 count[i]번 반복 출력
for i in range(1, 10001):
    for _ in range(C[i]):
        print(i)