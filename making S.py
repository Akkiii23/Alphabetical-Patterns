for n in range(7):
    for m in range(5):
        if (n==0 or n==3 or n==6)or (m==0 and(n>0 and n<3))or (m==4 and(n>3 and n<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
