import sys
input = sys.stdin.readline

def recursion(s, l, r, k):
    if l >= r: print(1, k)
    elif s[l] != s[r]: print(0, k)
    else: return recursion(s, l+1, r-1, k+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

T = int(input())
for _ in range(T):
  S = input().rstrip()
  isPalindrome(S)