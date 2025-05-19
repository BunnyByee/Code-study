n = int(input())
lst = []

for _ in range(n):
    data = input()
    lst.append(data)

# 중복 제거
lst = list(set(lst))

# 길이 기준 정렬 후, 길이가 같으면 사전순 정렬
lst.sort() # 일단 사전순 정렬
lst.sort(key=len) # 길이 기준 정렬

print(*lst, sep='\n')