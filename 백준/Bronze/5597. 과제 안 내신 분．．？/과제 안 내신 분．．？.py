n_list = [i for i in range(1, 31)]
# 제출한 28명 번호 받기
submit = [int(input()) for _ in range(28)]

# set(집합 자료형)으로 변경하여 차집합 구하기
no_submit = list(set(n_list) - set(submit))

# 오름차순 정렬 후 순서대로 출력
no_submit.sort()
print(no_submit[0])
print(no_submit[1])