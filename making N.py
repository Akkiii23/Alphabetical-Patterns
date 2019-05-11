for n in range(7):
    for m in range(7):
        if (m==0 or m==6) or (n-m==0):
            print("*",end="")
        else:
            print(end=" ")
    print()
