num = []

for _ in range(5):
    data = int(input())
    num.append(data)

num.sort()
result1 = sum(num) / len(num)
result2 = num[2]

print(int(result1))
print(result2)