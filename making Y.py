
# Reverse Y
'''
for n in range(7):
    for m in range(7):
        if (n-m==0 and n>3)or(n+m==6 and n>3)or (m==3 and n<4):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''

# Y

for n in range(7):
    for m in range(7):
        if (n-m==0 and n<4)or(n+m==6 and n<3)or (m==3 and n>3):
            print("*",end="")
        else:
            print(end=" ")
    print()
