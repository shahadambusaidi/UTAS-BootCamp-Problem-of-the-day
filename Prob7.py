#Prob7
'''Given an array of a positive intergers. Your task is to find the leader in the array.
An element of array is leader if it is greater than or equal to all the elements to it is right side.
The right most element is always a leader.
input n=6 , A[]=[16,17,4,3,5,2]
output : 17,5,2'''

    
# Python Function to print leaders in array
arr=[16, 17, 4, 3, 5, 2] 
def printLeaders(arr,size):   
    for i in range(0, size):
        for j in range(i+1, size):
            if arr[i]<=arr[j]:
                break
        if j == size-1: # If loop didn't break
            print (arr[i],end=' ')
 
# Driver function
printLeaders(arr, len(arr))


