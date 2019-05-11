# As per our requirement, get the pattern after entering the number of rows and columns. 

n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))
for i in range(1,n+1):
    for j in range(1,m+1):
        print("*", end = " ")
    print()
