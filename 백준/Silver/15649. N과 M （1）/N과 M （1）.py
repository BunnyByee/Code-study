# 1부터 N까지 자연수 중에서 중복 없이 m개를 고른 수열 (사전순서대로)
N, M = map(int, input().split())
path = [] # 경로 저장용 리스트
visited = [False] * (N+1) # 방문 여부 확인

def dfs(path):
    if len(path) == M :
        print(*path)
        return
    for i in range(1, N+1):
        if not visited[i] :
            visited[i] = True
            dfs(path + [i]) # 리스트에 i 추가
            visited[i] = False

dfs([])