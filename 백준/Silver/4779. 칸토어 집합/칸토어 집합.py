def cantor(arr, p, r):
  # 구간의 길이가 3 미만이면 종료
  if r - p < 3:
    return
  
  q =  (r - p) // 3
  
  for i in range(p + q, p + q*2) :
    arr[i] = ' '
  
  cantor(arr, p, p + q)
  cantor(arr, p + q*2, r)
  return arr

# 입력이 끝날 때까지 출력하기
while True :
  try:
    n = int(input())
    length = 3**n
    s = ['-'] * length

    cantor(s, 0, length)
    print(''.join(s))
  except EOFError:
    break