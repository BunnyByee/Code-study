from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

circle = deque(i+1 for i in range(n))
result = []

while True :
    # 큐가 다 비워질때까지 진행
    if len(circle) == 0 :
        break

    # k-1 번째까지 사람들을 다 뒤로 보내기
    for _ in range(k-1) :
        circle.append(circle.popleft())
    # k번째 값 리스트에 넣기
    result.append(circle.popleft())

print("<"+ ", ".join(map(str, result))+ ">")