n =int(input("Enter the number of rows:"))
for i in range(0,n):
    for j in range(0,n-i-1):    # For printing blanck spaces in the structure of pyramid.
        print(end="")
    for j in range(0,i+1):
        print("*",end="")
    print()
