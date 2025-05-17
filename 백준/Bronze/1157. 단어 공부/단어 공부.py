# 대소문자 구분 제거 & 대문자 출력 -> 모두 대문자로 바꿔버리기
str1 = input().upper()

# 중복 제거 (문자 카운트용)
str2 = list(set(str1))

n = 0
answer = ''

for i in str2 :
    if str1.count(i) > n :
        # n보다 크면 저장
        n = str1.count(i)
        answer = i
        # 횟수가 같은게 있으면 물음표 
    elif str1.count(i) == n :
        answer = '?'

print(answer)