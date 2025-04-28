s = input()
sum = 0
c = 0

for i in s :
    c = ord(i)
    if c >= 87 :
        sum += 10
    elif c >= 84 :
        sum += 9
    elif c >= 80 :
        sum += 8
    elif c >= 77 :
        sum += 7
    elif c >= 74 :
        sum += 6  
    elif c >= 71 :
        sum += 5
    elif c >= 68 :
        sum += 4
    elif c >= 65 :
        sum += 3

print(sum)