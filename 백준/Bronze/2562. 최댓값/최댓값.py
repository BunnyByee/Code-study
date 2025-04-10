n_list = [int(input()) for _ in range(9)]
n_max = n_list[0]
max_index = 0

for i in range(9) :
    if n_max < n_list[i] :
        # 최대값 및 인덱스 값 저장
        n_max = n_list[i]
        max_index = i

print(n_max)
print(max_index+1)