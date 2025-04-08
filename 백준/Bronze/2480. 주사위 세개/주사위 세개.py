a, b, c = map(int,input().split())

if (a == b and a == c) :
    print(10000 + a * 1000)
    
elif (a == b and a != c) : 
    s = a
    print(1000 + s * 100)
elif (b == c and a != b) :
    s = b
    print(1000 + s * 100)
elif (a == c and a != b) :
    s = a
    print(1000 + s * 100)

else :
    print(max(a,b,c)* 100)