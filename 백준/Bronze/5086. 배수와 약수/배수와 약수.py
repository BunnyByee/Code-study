# 0 0이 나올때까지 반복
while(True):
    a, b = map(int,input().split())
    if (a == 0 & b == 0):
        break
    # a < b -> a가 b의 약수인지 확인!
    elif (a < b) & (b % a == 0) :
        print("factor")
    # a > b -> a가 b의 배수인지 확인!
    elif (a > b) & (a % b == 0) :
        print("multiple")
    else :
        print("neither")