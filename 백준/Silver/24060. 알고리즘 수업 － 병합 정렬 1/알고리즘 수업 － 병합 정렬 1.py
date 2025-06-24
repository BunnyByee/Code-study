import sys
sys.setrecursionlimit(10**6) # 재귀 횟수 확장
input = sys.stdin.readline

count = 0
result = -1

def merge_sort(arr, p, r, k):
  global count, result
  if p < r:
      q = (p + r) // 2
      merge_sort(arr, p, q, k)
      merge_sort(arr, q + 1, r, k)
      merge(arr, p, q, r, k)

def merge(arr, p, q, r, k) :
  global count, result
  tmp = []
  i, j = p, q + 1

  while i <= q and j <= r :
    if arr[i] <= arr[j] :
      tmp.append(arr[i])
      i += 1
    else :
      tmp.append(arr[j])
      j += 1
  
  while i <= q :
    tmp.append(arr[i])
    i += 1
  
  while j <= r :
    tmp.append(arr[j])
    j += 1

  for t in range(len(tmp)):
    arr[p + t] = tmp[t]
    count += 1
    if count == K:
        result = tmp[t]

# main
N, K = map(int, input().split())
A = list(map(int, input().split()))

merge_sort(A, 0, N-1, K)
print(result)