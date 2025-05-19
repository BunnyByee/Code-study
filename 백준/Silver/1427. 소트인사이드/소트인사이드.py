# n 입력 받고, 리스트로 나누기
n = input()
num = list(n)
num.sort(reverse=True)

print(*num, sep='')