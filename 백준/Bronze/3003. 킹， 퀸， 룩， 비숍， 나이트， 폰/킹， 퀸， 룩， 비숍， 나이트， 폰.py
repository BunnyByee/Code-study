input_list = list(map(int, input().split()))
n_list = [1, 1, 2, 2, 2, 8]
result = 0

for i in range(len(n_list)) :
    result = n_list[i] - input_list[i]
    print(result, end=" ")