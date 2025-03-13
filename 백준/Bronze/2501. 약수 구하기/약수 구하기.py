n, k = map(int,input().split())
li = []
# a의 약수 구하기 (나머지가 0이면 약수) -> 리스트로 만들기
for i in range(1,n+1) :
    if n % i == 0 :
        li.append(i)
# 리스트에서 k-1 번째 값 가져오기 (리스트 개수보다 k가 크면 0)
print(li[k-1] if k <= len(li) else 0)