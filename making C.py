
# 1st Way to print as C
'''

for n in range(6):
    for m in range(5):
        if (n==0 or n==5 or m==0)or((m==1 or m==2 or m==3) and (n!=1 and n!=2 and n!=3 and n!=4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''


# 2nd Way to print as C

for n in range(6):
    for m in range(5):
        if (m==0 and (n!=0 and n!=5)) or ((n==0 or n==5) and (m>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
