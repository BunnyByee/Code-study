n = int(input())
lst = list(map(int, input().split()))

# 중복 제거 후 정렬, 딕셔너리로 연결
k = sorted(set(lst))
rank = {num: idx for idx, num in enumerate(k)}

for i in lst :
    print(rank[i], end=' ')