h, m = map(int, input().split())
t = int(input())

all = h * 60 + m + t
# 시간을 다 더해서 새로 계산하기
# h : 60으로 나눈 몫, m : 60으로 나눈 나머지
if all // 60 > 23 :
    h = all//60 - 24
else :
    h = all // 60

m = all % 60

print(f'{h} {m}')