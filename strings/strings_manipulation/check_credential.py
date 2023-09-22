'''

2. Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123 
     
     
'''

import re

#Enter username and password  
username="myname@sayur.com"
password="mnamesay123"

#check for "@" in the username
if '@' in username:
    #check if the username is valid
    if username.endswith(".com") or username.endswith(".edu") or username.endswith(".tech") or username.endswith(".org"):
        #check if the frist 2 chars of password match with the 1st and 3rd char of username
        if (password[0]==username[0]) and (password[1]==username[2]):
            #split username 
            username_split=username.split("@")
            beforeAt=username_split[0]
            afterAt=username_split[1]
            #check if password contains company name and numbers. If true password is correct
            if (password[2:5]==beforeAt[-3:]) and (password[5:8]==afterAt[:3]) and re.match(r'^\d{3}$', password[8:]):
                print("Password is correct")
            else:
                #password doesnt hv company name and numbers
                print("Wrong password. Password should contain company name and numbers")
        else:
            ("Wrong password.The first two letters not matching")
    else:
        print("Invalid username")
else:
    print("@ not found. Invalid username")