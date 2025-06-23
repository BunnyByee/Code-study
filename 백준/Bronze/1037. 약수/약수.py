import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 오름차순으로 정렬하기
a.sort()

# 약수 중 첫번째 값과 마지막 값을 곱하면 마지막 값이 나옴.
print(a[0] * a[-1])