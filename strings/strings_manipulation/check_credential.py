'''

2. Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123 
     
     
'''

import re

def is_valid_username(username):
    if re.match(r'.*@(.*\.(com|edu|tech|org))$', username):
        return username
    
def password:
    