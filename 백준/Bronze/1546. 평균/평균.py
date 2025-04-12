n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

new_scores = [(i / max_score) * 100 for i in scores]

total = 0
for s in new_scores :
    total += s

print(total/n)