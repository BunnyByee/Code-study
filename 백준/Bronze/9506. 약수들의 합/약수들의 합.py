while(True) :
    n = int(input())
    li = []
    sum = 0

    if n == -1 :
        break
        
    for i in range(1,n) :
        if n % i == 0 :
            li.append(i)
            sum += i

    if n == sum :
        print(f'{n} =', end=' ')
        for i in range(len(li)):
            if i == len(li) - 1 :
                print(li[i])
            else :
                print(f'{li[i]} + ', end='')
    else :
        print(f'{n} is NOT perfect.')