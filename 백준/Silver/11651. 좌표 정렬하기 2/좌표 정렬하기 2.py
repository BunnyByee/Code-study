n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda point: (point[1], point[0]))

for p in points:
    print(p[0], p[1])