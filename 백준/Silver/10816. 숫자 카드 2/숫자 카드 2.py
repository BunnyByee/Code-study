n = int(input())
n_list = list(map(int, input().split()))

count_dict = {}
for num in n_list:
    if num in count_dict :
        count_dict[num] += 1
    else :
        count_dict[num] = 1

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list :
    print(count_dict.get(i, 0), end=' ')