inputs = [int(input()) for _ in range(10)]

# 42로 나누었을 떄 나머지 set으로 저장
n_set = {(n % 42) for n in inputs}

print(len(n_set))