N = int(input())
cols = set()
diag1 = set()
diag2 = set()
cnt = 0

def dfs(row):
    global cnt
    # 종료조건
    if row == N :
        cnt += 1
        return 
    
    # 각 열마다 가능한지 확인
    for col in range(N) :
        # 조건 확인 (같은 열이거나, 왼쪽 대각선이거나, 오른쪽 대각선이라면)
        if col in cols or (row-col) in diag1 or (row+col) in diag2 :
            continue
        # 가능하면 퀸을 놓기
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row+col)

        # 다음 행 탐색
        dfs(row+1)

        # 다른 열도 탐색 : 백트래킹
        # 집합은 순서가 없기 때문에 값을 지정해서 제거
        cols.remove(col)
        diag1.remove(row-col)
        diag2.remove(row+col)

# 0행 부터 시작!
dfs(0)
print(cnt)