#Prob8
'''Given an array A of a positive  integers your task is to find
the leader in the array . An element of array is leader if it
is greater than or equal to all the elements to its right side .
the right most element is always a leader.''' 

def find_leaders(arr):
    n = len(arr)
    max_right = arr[n - 1]  
    leaders = [max_right]

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders.append(max_right)

    leaders.reverse()  # Since we built the list in reverse order, we reverse it to get the correct order

    return leaders

# Example array
A = [16, 17, 4, 3, 5, 2]
leaders = find_leaders(A)
print("Leaders:", leaders)