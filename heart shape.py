
for i in range (1,7):
    for j in range (1,8):
        if (i==0 and j % 3 != 0) or (i==1 and j % 3 == 0) or(i - j == 2) or (i + j == 8):
            print("*",end="")
        else:
            print(" ",end="")
        print()
