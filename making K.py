for n in range(7):
    for m in range(5):
        if (m==0) or (n-m==2)or(n+m==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
