for n in range(7):
    for m in range(7):
        if (m==0 or m==6) or ((n==m)and(m>0 and m<4)or (n==2 and m==4) or(n==1 and m==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
