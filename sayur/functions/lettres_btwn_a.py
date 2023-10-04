'''

Problem 1
In the input, find the first A and last A, print all the letters between these two A.
'''

'''
def function PrintLettersBetweenAs
1. give input
2. find first a and its index
3. find second a and its index
4. print the letters in the index between the a's index

'''


def PrintLettersBetweenAs(aString): #fun def
    aString=aString.lower()  #concerting to lowercase
    first_a=string.find("a")
    if first_a>1:   #if only first a present find last a
        last_a=string.rfind("a")
        if(first_a!=last_a):   #if both are equal no letters between
            print(string[first_a+1:last_a])
        else:
            print("No letters in between the a since there is no second a")
            
    else:
        print("No a")
            
 
string=input("Enter the string: ")
str=PrintLettersBetweenAs(string)  #calling function


'''
Expected output:

Enter the string: I am Ciciya
m Ciciy

'''