'''
problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function
'''

#enter the 2 strings
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

if len(str1) != len(str2):# check if lengths are equal,if no its not same
    print(f"{str1} is not same as {str2}")
    
else:
    str=str1 +str1 #adding both the strings so that you will get a continuous pattern from which you can see if the second string matches
    if str2 in str: #check if str2 is in the concatenated string
        print(f"{str1} is same as {str2}")
    else:
        print(f"{str1} is not same as {str2}")
        
'''
OUTPUT
Enter the first string: 12345
Enter the second string: 34512
12345 is same as 34512
'''

#same as the previous one but with slicing
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

if len(str1) != len(str2):
    print(f"{str1} is not same as {str2}")
    
else:
    for i in range(len(str1)):
        str=str1[i:]+str1[:i]
        if str2 in str:
            print(f"{str1} is same as {str2}")
            break
        
    else:
        print(f"{str1} is not same as {str2}")
        
'''
OUTPUT:
Enter the first string: ciciya
Enter the second string: ciyaci
ciciya is same as ciyaci
'''
