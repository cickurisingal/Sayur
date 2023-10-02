'''

Program to calculate Collatz Conjecture using functions

'''
def CollatzConjecture(num): # defining the function
    count=0
    while(num>1):  # we need till it raeches 1
        
        if num%2==0: #even
            num=num/2
        else:
            num=num*3+1 #odd
        
        count+=1
    return count  #returning count to the place where the function is called
    
num1=int(input("Enter first number: ")) #first no.
num1_count=CollatzConjecture(num1) #calling fun.
print(f'No of iterations of {num1} is {num1_count}')

num2=int(input("Enter second number: "))  # secind no.
num2_count=CollatzConjecture(num2)
print(f' No of iterations of {num2} is {num2_count}')

if num1_count < num2_count :  #comparing the no. of iterations
    print(f'{num1} has undergone minimum iterations of  {num1_count} ')
else:
    print(f'{num2} has undergone minimum iterations of {num2_count}')

'''
Expected output:

Enter first number: 12
No of iterations of 12 is 9
Enter second number: 15
No of iterations of 15 is 17
12 has undergone minimum iterations of  9  

'''