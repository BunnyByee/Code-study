n = int(input())
n_list = list(map(int, input().split()))
n_max = n_list[0]
n_min = n_list[0]

for i in n_list :
    if n_max < i :
        n_max = i
    if n_min > i :
        n_min = i

print(f"{n_min} {n_max}")