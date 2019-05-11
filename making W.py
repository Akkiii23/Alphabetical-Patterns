for n in range(4):
    for m in range(7):
        if (m==0 or m==6)or(n+m==3)or(m-n==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
