from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 풍선 번호와 이동 값을 함께 deque로 구성 (번호는 1부터 시작)
circle = deque((i+1, num) for i, num in enumerate(nums))
result = []

while circle :
    idx, move = circle.popleft()
    result.append(idx)

    # 마지막 하나 남은거 받고 예외처리
    if not circle:
        break

    # 풍선 값이 양수면 왼쪽으로 회전
    if move > 0 :
        circle.rotate(-(move - 1))
    # 풍선 값이 음수면 오른쪽으로 회전
    else :
        circle.rotate(-move)

print(*result)