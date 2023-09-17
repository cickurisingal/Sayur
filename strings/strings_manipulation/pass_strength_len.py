'''
String manipulation exercises. Use builtin functions as needed.

1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
   strong - at least three alphabets, two numbers and one special char
   Very strong - same as strong, but at least 16 count
   All passwords must be at least 8 chars long. You can use RegEx if you want.
'''
import re

#input password
password=input("Enter the password: ")
password_len=len(password)
alpha_len=len(re.findall(r'[a-zA-Z]',password))
num_len=len(re.findall(r'[0-9]',password))
specialchar_len=len(re.findall(r'[^a-zA-Z0-9]',password))

#check if the password length is greater than 8
if password_len>8:
    if (alpha_len==password_len) or (num_len==password_len) or (specialchar_len==password_len):
        print("Weak password")
    elif (alpha_len>3)and (num_len>2) and (specialchar_len>1):
        if password_len> 16:
            print("Very strong password")
        else:
            print("Strong password")
    elif (alpha_len>1) and (num_len>1) and (specialchar_len>1):
        print("OK Password")
else:
    print("Weak password")