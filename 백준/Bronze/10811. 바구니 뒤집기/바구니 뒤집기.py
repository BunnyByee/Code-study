n, m = map(int, input().split())
n_list = [k for k in range(1, n+1)]

for _ in range(m):
    i,j = map(int,input().split())
    # 리스트 슬라이싱해서  특정 구간 뒤집기
    n_list[i-1:j] = n_list[i-1:j][::-1]

for s in n_list:
    print(s, end=" ")