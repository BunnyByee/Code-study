n = int(input())
str_list = [input() for _ in range(n)]
answer = 0

# 리스트 반복
for str in str_list :
    # 중복 확인용 list, 확인용 문자는 첫번째값 디폴트
    check_str1 = []
    char1 = str[0]

    for i in str :
        # list에 존재하지 않으면 추가 (처음 나오는 문자)
        if i not in check_str1 :
            check_str1.append(i)
        # 리스트에 존재하면 이전 문자 비교해서 -> 연속 문자가 아니면 종료
        else :
            if i != char1 :
                break
        
        # 이전 문자 확인용으로 저장
        char1 = i

    else :
        # 그룹문자 판별 성공시 카운트
        answer += 1

print(answer)