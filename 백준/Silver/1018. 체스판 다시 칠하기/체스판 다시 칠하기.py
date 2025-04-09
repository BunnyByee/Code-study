n, m = map(int, input().split())
chess = [input() for _ in range(n)]
min_count = float('inf')


for i in range(n - 7) :
    for j in range(m - 7) :
        w_start = 0  # 시작이 W인 경우 다시 칠해야 할 칸 수
        b_start = 0 

        for x in range(8):
            for y in range(8):
                current = chess[i + x][j + y]

                # (x + y)의 합이 짝수면, 시작 색과 같아야 하고
                # 홀수면, 시작 색과 반대여야 한다
                if (x + y) % 2 == 0:
                    if current != 'W':
                        w_start += 1
                    if current != 'B':
                        b_start += 1
                else:
                    if current != 'B':
                        w_start += 1
                    if current != 'W':
                        b_start += 1

        # 최소값 갱신
        min_count = min(min_count, w_start, b_start)
print(min_count)