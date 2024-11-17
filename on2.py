def abc(n):
    a = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
            a = i + 1
        print("")
    print(a)
abc(10)
abc(20)            