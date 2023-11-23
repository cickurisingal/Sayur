'''

In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B after the first A (if there is a A)
  and last B and print all the letters between these two B. 
  
  If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) 
  and last C and print all the letters between these two C.
  
  create a lambda function that multiplies argument x with argument y and prints the result
  
  create a lambda function that multiplies argument x with argument y and prints the result- lambda functios - sort by name, sort by cost
  
  solve cafe problem using dictionary instead of different lists
  
'''

def FindLetters(aString,alpha):
    aString=aString.lower()
    alpha=alpha.lower()
    firstIndex=aString.find(alpha)
    if (firstIndex>=0):
        