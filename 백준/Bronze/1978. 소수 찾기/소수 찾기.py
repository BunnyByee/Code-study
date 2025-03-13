k = int(input())
n_list = list(map(int, input().split()))

answer = []
for n in n_list :
    count = 0

    for j in range(1, n+1):
        if n % j == 0 :
            count += 1
    
    if (count == 2):
        answer.append(n)

print(len(answer))