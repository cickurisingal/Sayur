'''

Write a program for Collatz_conjecture.
# Collatz_conjecture means -  start with the input number. 
# For even number , divide by 2 (n/2)
# For odd number - 3n + 1
# apply the above for the result number until the answer is 1

'''


#give input number
n=int(input("Enter the number: "))
num=n

#initializing variable count
count=0

while n!=1:  #since we need to iterate till we get 1
    if n%2==0:  #if even
        n=n//2 #// is to get the proper integer value
    else:
        n=n*3+1  #if odd
        
    count+=1
    
print(f"The number {num} becomes 1 in {count} iterations")
    
    
'''

Expected output: 

Enter the number: 17
The number 17 becomes 1 in 12 iterations

'''