N, M = map(int, input().split())
path = []

def dfs(start, path) :
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N+1):
        path.append(i) # 리스트에 i 추가
        dfs(i, path)
        path.pop()

dfs(1, [])