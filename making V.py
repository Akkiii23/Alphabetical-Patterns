for n in range(4):
    for m in range(7):
        if (n-m==0)or (n+m==6):
            print("*",end="")
        else:
            print(end=" ")
    print()
