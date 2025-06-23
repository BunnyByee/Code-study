import sys
input = sys.stdin.readline

# 단어의 개수 n, 단어의 길이 기준 m
N, M = map(int, input().split())
words = {}

for _ in range(N):
  word = input().rstrip()

  # M 이상일때 딕셔너리 등록
  if len(word) >= M :
    if word not in words : # 존재하지 않으면?
      words[word] = [len(word), 1]
    else :             # 존재한다면 +1 -> 인덱스를 덧 붙이면 value 리스트에 접근 가능
      words[word][1] += 1

# 형태 => ('단어' , [단어 길이, 단어 개수])
# 순서 : 자주 나오는 단어 > 단어의 길이가 길수록 > 알파벳 사전 순
sorted_dict = sorted(words.items(), key = lambda x : (-x[1][1], -x[1][0], x[0]))

# key 만 출력
for k,v in sorted_dict :
  print(k)