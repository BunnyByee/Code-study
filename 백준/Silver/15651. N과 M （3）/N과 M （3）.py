# 메모리 최적화 코드
N, M = map(int, input().split())
path = []

def dfs(path) :
    if len(path) == M:
        print(*path)
        return
    
    for i in range(1, N+1):
        path.append(i) # 리스트에 i 추가
        dfs(path)
        path.pop()

dfs([])