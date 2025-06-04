from collections import deque
import sys

n = int(sys.stdin.readline())

queue = deque(i+1 for i in range(n))

while True :
    # 한 장의 카드가 남을때까지 진행 -> 마지막 카드 출력
    if len(queue) == 1 :
        print(*queue)
        break

    # 맨 앞장 카드는 버리고, 그다음 장 카드는 맨 뒤로 보내기
    queue.popleft()
    queue.append(queue.popleft())