# 응시자 수, 상받는 수, 점수 입력 받기
n, k = map(int, input().split())
score = list(map(int, input().split()))

# 내림차순 정렬해서 상받는 수 -1 번째가 커트라인
score.sort(reverse=True)

print(score[k-1])