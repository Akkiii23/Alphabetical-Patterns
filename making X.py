for n in range(5):
    for m in range(5):
        if (n-m==0)or(n+m==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
