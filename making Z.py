for n in range(7):
    for m in range(7):
        if (n==0 or n==6 or n+m==6): 
            print("*",end="")
        else:
            print(end=" ")
    print()
