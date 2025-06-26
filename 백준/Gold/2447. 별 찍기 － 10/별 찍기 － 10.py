import sys

def star(arr, x, y, size) :
    if size == 1:
        return
    
    # 나눈다 (3x3)
    n_size = size // 3

    # 가운데 정사각형 비우기
    for i in range(x + n_size, x + n_size*2) :
        for j in range(y + n_size, y + n_size*2):
                arr[i][j] = ' '

    # 3x3 구역 순회하면서 가운데 빼고 재귀 호출
    for dx in range(3):
        for dy in range(3):
            if dx == 1 and dy == 1:
                continue  # 가운데는 스킵
            star(arr, x + dx * n_size, y + dy * n_size, n_size)

    return arr

# MAIN 코드
n = int(sys.stdin.readline())
arr = [['*' for _ in range(n)] for _ in range(n)]
# arr = [['*']*3]*3 : 같은 메모리 공유하므로 이렇게 하면 안 됨.

star(arr, 0, 0, n)

for row in arr:
    print(''.join(row))