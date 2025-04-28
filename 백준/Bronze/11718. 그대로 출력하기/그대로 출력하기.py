while True :
    try:
        a = input()

        print(a)

        if (a == '') :
            break
    except EOFError :
        break