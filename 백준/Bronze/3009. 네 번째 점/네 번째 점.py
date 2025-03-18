arrA = []
arrB = []
y = {}

def countNum(arrN):
    x = {}
    for i in arrN:
        try:
            x[i] += 1
        except:
            x[i] = 1

    for k, v in x.items():
        if v == 1 :
            return k

for _ in range(3):
    a, b = map(int, input().split())
    arrA.append(a)
    arrB.append(b)

print(countNum(arrA), end=" ")
print(countNum(arrB))