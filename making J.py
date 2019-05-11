for n in range(7):
    for m in range(4):
        if (m==3) or (n==6)or (m==0 and (n!=0 and n!=1 and n!=2 and n!=3)):
            print("*",end="")
        else:
            print(end=" ")
    print()
