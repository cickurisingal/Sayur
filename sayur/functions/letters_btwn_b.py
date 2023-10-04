'''
In the input, find the first A and last A, print all the letters between these two A.
Also print the letters between first B and last B

'''

def LetterBetweenAlpha(aString,alpha):
    aString=aString.lower()
    alpha=alpha.lower()
    first_alpha=aString.find(alpha)
    if (first_alpha>=0):
        last_alpha=aString.rfind(alpha)
        if (first_alpha!=last_alpha):
            print(f'The letters between the two "{alpha}"s are "{aString[first_alpha+1:last_alpha]}"')
        else:
            print(f'No second {alpha} in the string')
    else:
        print(f'No {alpha}')

string=input("Enter the string: ")
alphabet=input("Enter the character: ")
LetterBetweenAlpha(string,alphabet)

'''
Expected output: 

Enter the string: Baloons are big
Enter the character: a
The letters between the two "a"s are "loons "

Enter the string: Baloons are big
Enter the character: b
The letters between the two "b"s are "aloons are "

'''