n = int(input())
points = []

for _ in range(n):
    x, y = map(int,input().split())
    # 튜플 형태로 저장
    points.append((x,y))

# 튜플 정렬
points.sort()

for p in points:
    print(p[0], p[1])