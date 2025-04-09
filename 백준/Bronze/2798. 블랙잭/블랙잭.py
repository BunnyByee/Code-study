n, m = map(int,input().split())
numbers = list(map(int,input().split()))
result = 0

for i in range(n) :
    for j in range(i + 1, n) :
        for k in range(j + 1 , n) :
            n_sum = numbers[i] + numbers[j] + numbers[k]
            if n_sum <= m :
                # 최대값 비교
                result = max(result, n_sum)

print(result)