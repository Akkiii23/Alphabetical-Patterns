for n in range(8):
    for m in range(6):
        if (m==0 and n!=7 )or (m==4 and n!=7)or (n==0 and m!=5) or (n==6 and m!=5)or (n==4 and m==2) or (n==5 and m==3)or (n==7 and m==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
