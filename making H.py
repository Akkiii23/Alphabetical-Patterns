for n in range(7):
    for m in range(4):
        if (m==0 or m==3 or n==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
