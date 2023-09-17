'''
String manipulation exercises. Use builtin functions as needed.

1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
   strong - at least three alphabets, two numbers and one special char
   Very strong - same as strong, but at least 16 count
   All passwords must be at least 8 chars long. You can use RegEx if you want.
'''

import re  #re=regualar expression

#imput password
password=input(" Enter the password: ")

#check if len of password is greater than 8

if len(password)<8:
    print("Password is too short. It must be of 8 characters")
    
else:
    # weak if it contains only alphabets
    if re.match("^[a-zA-Z]+$",password):
        print("Weak password-only alphabets")
    # weak if it contains only numbers
    elif re.match("^[0-9]+$",password):
        print("Weak password-only numbers")
    # weak if it contains only special characters
    elif re.match("^[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]+$",password):
        print("Weak password-only special characters")
     #else check if it contains alphabets, numbers and special characters   
    elif re.match("^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\-])", password):
        if len(re.findall("[a-zA-Z]",password))>=3 and len(re.findall("[0-9]",password))>=2 and len(re.findall("[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]",password))>=1:
            #if password contains more than 16 characters it is very strong
            if len(password)>16:
                print("Very strong password")
            else:
                print("Strong password")
        else:
            print("OK password. Not much characters")
    else:
        print("Weak password")
        
        
        
#OUTPUT
#Enter the password: ciciya@2002
#Strong password
    
    
