n, m = map(int,input().split())

name_to_num = {}
num_to_name = {}

# dict = map을 활용한 키-값 형태 등록
for i in range(1, n+1):
    name = input()
    name_to_num[name] = i
    num_to_name[i] = name

# 문제 m개, 값 출력
for _ in range(m):
    query = input()

    # 문자열이 숫자면, 문자 출력
    if query.isdigit() :
        print(num_to_name[int(query)])
    # 문자면, 숫자 출력
    else :
        print(name_to_num[query])