
# 1st Way to print D

'''
for n in range(7):
    for m in range(6):
        if (m==0 or m==5)or((n==0 or n==6)and (m>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''

# 2nd Way to print D

for n in range(7):
    for m in range(6):
        if (m==0) or(m==5 and (n!=0 and n!=6))or((n==0 or n==6)and (m>0 and m<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
