
# Make the shape as B
'''

for n in range(7):          # n = number of rows
    for m in range(5):      # m = mumber of columns
        if (m==0 or m==4) or ((n==0 or n==3 or n==6) and (m>0 and m<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
        
'''


# Another way to make the shape B

for n in range(7):          # n = number of rows
    for m in range(5):      # m = mumber of columns
        if (m==0)or (m==4 and (n!=0 and n!=3 and n!=6)) or ((n==0 or n==3 or n==6) and (m>0 and m<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
        
