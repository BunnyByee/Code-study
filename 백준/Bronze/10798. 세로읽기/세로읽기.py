list1 = []

for _ in range(5):
    list1.append(input())

max_len = max(len(row) for row in list1)

for i in range(max_len):
    for j in range(5):
        if i < len(list1[j]) :
            print(list1[j][i], end='')