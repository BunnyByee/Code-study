import sys
input = sys.stdin.readline

n = int(input())

dancing = {'ChongChong'}

for _ in range(n):
  a, b = input().split()
  
  # 춤추는 사람인지 확인하고 넣기 (어차피 set은 중복제거가 됨)
  if a in dancing or b in dancing :
    dancing.add(a)
    dancing.add(b)

print(len(dancing))