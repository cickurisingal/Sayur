'''
Find letters between first and last A. If no A or no two A,
then find letters between first and last B
'''



def LetterBetweenAlpha(aString,alpha):
    aString=aString.lower()
    alpha=alpha.lower()
    alphaFound=False
    first_alpha=aString.find(alpha)
    if (first_alpha>=0):
        last_alpha=aString.rfind(alpha)
        if (first_alpha!=last_alpha):
            print(f'The letters between the two "{alpha}"s are "{aString[first_alpha+1:last_alpha]}"')
            alphaFound=True
        else:
            print(f'No second {alpha} in the string')
    else:
        print(f'No {alpha}')
        
    return alphaFound

string=input("Enter the string: ")

if(LetterBetweenAlpha(string,alpha="a")!=True):
    LetterBetweenAlpha(string,alpha="b")
    
    
'''
Expected output:

Enter the string: Baloons are big
The letters between the two "a"s are "loons "

Enter the string: Big Boss
No a
The letters between the two "b"s are "ig "


'''