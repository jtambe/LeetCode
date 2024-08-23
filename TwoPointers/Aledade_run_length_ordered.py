'''
Question: Write a python3 function: def solution(A, Y) that accepts as arguments a list of integers and an integer run length. It must ﬁnd in that list all runs of run length consecutive numbers that increase or decrease by 1. It should return the list indices of the ﬁrst element of each run. If there are no consecutive runs it should return an empty list. Feel
Write a python3 function:

def solution(A, Y)

that accepts as arguments a list of integers and an integer run length. It must ﬁnd in that list all runs of run length consecutive numbers that increase or decrease by 1. It should return the list indices of the ﬁrst element of each run. If there are no consecutive runs it should return an empty list.

Feel free to rename the arguments in the function signature, e.g.: def solution(values, run_length):

Example: values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7,8,7], run_length=3 returns [0, 4, 6, 7]

Additionally, please give comments on the code's runtime and space complexity.
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
I am going to divide this problem in 3 parts
1. Get a list of index numbers for increasing numbers
2. Get a list of index numbers for decreasing numbers
3. Since this solution expects an ordered list, I will merge above two lists in order

Assumption:
1. run_length cannot be less than 2 since we would require minimum 2 numbers to compare
1. I am assuming that for edge cases, we want to return empty list


RunTime Complexity: 
O(n) = O(n) for increasing list + O(n) for decreasing list + O(n) for merging lists in order

Space Complexity: 
O(n) = maximum space needed to store answer list including increasing and decreasing lists will be O(n-1).
"""

from typing import List

def solution(A, Y):

    print(A, Y)
    # explicit check for edge cases to save further computations
    # empty list or run_length < 2 or run_length > len(list)
    if (len(A) == 0 or Y < 2 or Y > len(A)):
        return []

    # increasing index numbers list
    # O(n)
    increasing = increasingList(A, Y)

    # decreasing index numbers list
    # O(n)
    decreasing = decreasingList(A, Y)

    # # add two lists & sort
    # # O(nlogn)
    # ans = increasing + decreasing
    # ans.sort()

    # merge the two lists
    # O(n)
    ans = mergeListsInorder(increasing, decreasing)

    return ans


def increasingList(A:List[int], Y:int) -> List[int]:
    """ 
    Returns a list of index numbers for increasing sequence
    param A: list of values
    param Y: run length
    """
    increasing: List[int] = []
    l,r, count = 0, 0, 0
    while (r < len(A)-1):
        # if consecutive numbers are increasing, we increment the right pointer & counter
        # once we find increasing run_length, we just move left pointer
        if (A[r] + 1 == A[r+1]):
            r += 1
            count += 1
            if (count == Y-1):
                increasing.append(l)
                count -= 1
                l += 1
        # if consecutive numbers are not increasing, we simply move both pointers
        # additionally, we mark count = 0 to wipe off counter because of previous run_length data
        else:
            r += 1
            l = r
            count = 0
    return increasing

def decreasingList(A:List[int], Y:int) -> List[int]:
    """ 
    Returns a list of index numbers for decreasing sequence
    param A: list of values
    param Y: run length
    """
    decreasing: List[int] = []
    l,r, count = 0, 0, 0
    while (r < len(A)-1):
        # if consecutive numbers are decreasing, we increment the right pointer & counter
        # once we find decreasing run_length, we just move left pointer
        if (A[r] - 1 == A[r+1]):
            r += 1
            count += 1
            if (count == Y-1):
                decreasing.append(l)
                count -= 1
                l += 1
        # if consecutive numbers are not decreasing, we simply move both pointers
        # additionally, we mark count = 0 to wipe off counter because of previous run_length data
        else:
            r += 1
            l = r
            count = 0
    return decreasing
    
def mergeListsInorder(increasing: List[int], decreasing: List[int]) -> List[int]:
    """ 
    Returns a list of merged sequences in ascending order
    param increasing: list of increasing index numbers
    param decreasing: list of decreasing index numbers
    """
    
    #edge case
    # if one or both lists are empty
    if (len(increasing) == 0):
        return decreasing
    if (len(decreasing) == 0):
        return increasing
    
    
    ans: List[int] = []
    # left pointer for increasing length
    # right pointer for decreasing length
    # while the smallest list has values, compare numbers in two lists and add smaller number in answer
    # increment the correct pointer
    l,r = 0,0
    while (l < len(increasing) and r < len(decreasing)):
        if (increasing[l] < decreasing[r]):
            ans.append(increasing[l])
            l += 1
        else:
            ans.append(decreasing[r])
            r += 1

    # once the smallest list is complete, merge rest of the values from larger list
    if (len(decreasing[r:]) > 0):
        ans.extend(decreasing[r:])
    if (len(increasing[l:]) > 0):
        ans.extend(increasing[l:])
    
    return ans
    


values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7,8,7]
run_length=3
ans = solution(values, run_length)
print(f"ans:{ans}")

values=[3, 2, 5, 6]
run_length=2
ans = solution(values, run_length)
print(f"ans:{ans}")

values=[1,2,3,4]
run_length=2
ans = solution(values, run_length)
print(f"ans:{ans}")

values=[1, 2, 3, 5]
run_length=3
ans = solution(values, run_length)
print(f"ans:{ans}")

values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7,8,7]
run_length=2
ans = solution(values, run_length)
print(f"ans:{ans}")


values=[1, 2, 3, 5]
run_length=12
ans = solution(values, run_length)
print(f"ans:{ans}")

values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7,8,7]
run_length=1
ans = solution(values, run_length)
print(f"ans:{ans}")

values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7,8,7]
run_length=0
ans = solution(values, run_length)
print(f"ans:{ans}")

