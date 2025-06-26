cnt = 0
moves = []

def hanoi(n, start, end, sub):
    global cnt
    if n == 1 : # 1개면 바로 도착지로
        moves.append((start, end))
        cnt += 1
        return
    
    # n-1 개의 원판을 보조기둥으로 보냄
    hanoi(n-1, start, sub, end)
    # 가장 큰 원판을 옮기기
    moves.append((start, end))
    cnt += 1
    # 보조에 있는 n-1개의 원판을 도착지로 보냄
    hanoi(n-1, sub, end, start)

N = int(input())
total = hanoi(N, 1, 3, 2)

print(cnt)
for s,e in moves:
    print(s,e)