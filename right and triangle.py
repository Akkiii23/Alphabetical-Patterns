
# Making the pattern in right angle triangle.

'''
n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end = " ")  # for printing * horizontally
    print()                    # for printing * verically
'''



# Using While loop

'''
n = int(input("Enter the number:"))
i = 1
while i <= n:
    print(' * ' *i)
    i = i + 1
'''

# Right angle triangle in downword direction

n = int(input("Enter the number:"))
i = 1
while i <= n:
    print(' * ' *n)
    n = n - 1
