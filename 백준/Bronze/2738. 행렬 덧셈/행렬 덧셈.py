# axb 행렬 만들기
a, b = map(int, input().split())

def input_matrix(rows):
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# 행렬 두개 생성
m1 = input_matrix(a)
m2 = input_matrix(a)

# 행렬 합
result = []

for i in range(a) :
    row = []
    for j in range(b):
        row.append(m1[i][j] + m2[i][j])
    result.append(row)

for r in result :
    print(*r)