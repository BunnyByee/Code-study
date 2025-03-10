Paper = [[0]*100 for col in range(100)]

a = int(input())

for _ in range(a):
    w, h = map(int, input().split())
    for i in range(w, w+10):
        for j in range(h, h+10):
            Paper[i][j] = 1

answer = 0

for i in range(100):
    answer += sum(Paper[i])
print(answer)