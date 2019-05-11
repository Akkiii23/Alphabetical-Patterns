for n in range(7):
    for m in range(7):
        if (m==0) or (m==4 and (n!=0 and n!=1 and n!=2))or (n==0) or (n==6 and (m!=5 and m!=6)) or (n==3 and (m!=1 and m!=2 and m!=6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
