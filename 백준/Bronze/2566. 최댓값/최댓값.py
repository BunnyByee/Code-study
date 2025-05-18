# 9x9 배열 만들기
matrix = []
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

# 최댓값 찾기
max_val = -1
r , c = 0, 0
for i in range(9) :
    for j in range(9):
        # 최댓값이면
        if matrix[i][j] > max_val :
            max_val = matrix[i][j]
            r = i
            c = j

print(max_val)
print(r+1, c+1)