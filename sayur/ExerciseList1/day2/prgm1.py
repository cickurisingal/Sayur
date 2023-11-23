'''

Problem #1
Print the following pattern
1
212
32123
4321234
543212345
Get user input for how far to go (up to 0)
'''

num_rows = int(input("Enter the number of rows: "))

for i in range(1, num_rows + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    for k in range(2, i + 1):
        print(k, end="")
    print()
