for n in range(7):
    for m in range(4):
        if (m==0)or (n==0 or n==6 or n==3) and (m>0 and m<4):
            print("*",end="")
        else:
            print(end=" ")
    print()
