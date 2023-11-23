'''
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row
'''

def print_pattern(rows):
    for i in range(rows):
        # Print characters
        for j in range(i + 1):
            print(chr(97 + j), end="")
        
        # Print characters in reverse order
        for k in range(i - 1, -1, -1):
            print(chr(97 + k), end="")
        
        print()

# Call the function with the number of rows you want
print_pattern(7)