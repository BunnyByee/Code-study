in1 = int(input())
in2 = int(input())

if (in1 > 0) & (in2 > 0 ) :
    print(1)
elif (in1 < 0) & (in2 > 0) :
    print(2)
elif (in1 < 0) & (in2 < 0) :
    print(3)
elif (in1 > 0) & (in2 < 0) :
    print(4)