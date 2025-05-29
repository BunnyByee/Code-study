# gcd (유클리드 활용)
def gcd(a,b):
    while b != 0 :
        a, b = b, a%b
    return a

n = int(input())
tree = [int(input()) for _ in range(n)]

# 가로수 간격 구하기
diffs = []
for i in range(1, n): # 뒤에 값에서 앞에 값 빼기
    diffs.append(tree[i] - tree[i-1])

# 간격의 최대공약수 구하기
g = diffs[0]
for i in diffs[1:] :
    g = gcd(g, i)

# 전체 구간을 최대공약수로 나눠서 전제 개수 구하기
tree_add = (tree[-1] - tree[0]) // g + 1

# 원래 심어진 개수 빼기
print(tree_add-n)