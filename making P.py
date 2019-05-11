for n in range(7):
    for m in range(5):
        if (m==0)or (m==4 and (n<4))or (n==0 or n==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
