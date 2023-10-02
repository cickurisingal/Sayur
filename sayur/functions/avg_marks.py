
'''
Problem 1:
Write a program to calculate your avg marks in CS subject in the last 3 exams.
'''

'''
1. def functions:
      input: 3 marks
          avg= sum/3
      output:avg mark
      
2. Take 3 input marks..
3. Print average as output
      
'''
#defining function
def avg_marks(mark1,mark2,mark3):
    avg=(mark1+mark2+mark3)/3
    return avg


#3 input
mark1=int(input("Enter first mark: "))
mark2=int(input("Enter second mark: "))
mark3=int(input("Enter third number: "))

average= avg_marks(mark1,mark2,mark3) #calling function
print(f"Average of 3 marks is {average}")


'''
Expected output:

Enter first mark: 24
Enter second mark: 23
Enter third number: 25
Average of 3 marks is 24.0    
'''