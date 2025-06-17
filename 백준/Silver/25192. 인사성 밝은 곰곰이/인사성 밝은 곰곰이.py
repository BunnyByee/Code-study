import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
nickname_set = set()

for _ in range(n):
  chat = input().rstrip()
  # ENTER 이후로 새로운 사람 입장 -> 곰곰티콘 사용 확인 (초기화)
  if chat == 'ENTER' :
    nickname_set.clear()
  
  # ENTER가 아니고 stack 에 존재하지 않으면 push, cnt + 1
  if chat not in nickname_set and chat != 'ENTER' :
    nickname_set.add(chat)
    cnt += 1

print(cnt)