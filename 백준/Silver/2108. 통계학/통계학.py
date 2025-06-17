from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

# 산술평균 : 소수점 이하 첫째 자리에서 반올림한 값 출력
print( round( sum(data) / n ) )

# 중앙값 : n은 홀수이기 때문에 가운데 값을 찾아서 출력
print( data[n//2] )

# 최빈값
counter = Counter(data)
most_common = counter.most_common()
max_freq = most_common[0][1]  # 최빈값의 빈도수

# 최빈값 리스트 만들기
mode_list = [num for num, freq in most_common if freq == max_freq]

# 여러 개면 두 번째로 작은 값 출력, 하나면 그냥 출력
if len(mode_list) > 1:
    mode_list.sort()
    print(mode_list[1])
else:
    print(mode_list[0])

# 범위 : 최대값 - 최소값
print(data[-1] - data[0])