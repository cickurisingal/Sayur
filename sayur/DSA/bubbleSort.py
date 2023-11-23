'''
Bubble sort

'''
#defining function
def bubbleSort(num):
    #initializing n as length of array
    n=len(num)
    for i in range (n): # i is iterated till the length of the array
        for j in range(0,n-1): # the last digit will already bw sorted so till "n-1"
            if num[j] > num[j+1]: # comparing the 2 adjacent numbers
                #swapping the numbers
                num[j],num[j+1]=num[j+1],num[j]
                
    print("Sorted array is ",num)
    
num=[12,23,45,32,12]
print("Given array to sort is", num)
bubbleSort(num)