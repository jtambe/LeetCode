'''
def checkIncreasingY(nums: List[int]) -> bool:
    i = 1
    while(i < len(nums)):
        if(nums[i]-nums[i-1] != 1):
            return False
    return True

def checkDecreasingY(nums: List[int]) -> bool:
    i = 1
    while(i < len(nums)):
        if(nums[i-1]-nums[i] != 1):
            return False
    return True


Question: Write a python3 function: def solution(A, Y) that accepts as arguments a list of integers and an integer run length. It must ﬁnd in that list all runs of run length consecutive numbers that increase or decrease by 1. It should return the list indices of the ﬁrst element of each run. If there are no consecutive runs it should return an empty list. Feel
Write a python3 function:

def solution(A, Y)

that accepts as arguments a list of integers and an integer run length. It must ﬁnd in that list all runs of run length consecutive numbers that increase or decrease by 1. It should return the list indices of the ﬁrst element of each run. If there are no consecutive runs it should return an empty list.

Feel free to rename the arguments in the function signature, e.g.: def solution(values, run_length):

Example: values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7,8,7], run_length=3 returns [0, 4, 6, 7]

Additionally, please give comments on the code's runtime and space complexity.
'''

from typing import List

def solution(A: List[int], Y: int) -> List[int]:
    ans: List[int] = []

    # Increasing list
    # O(n)
    increasing = IncreasingList(A, Y)

    # Decreasing list
    # O(n)
    decreasing = DecreasingList(A, Y)
    
    #ans.sort()
    # Merge increasing and decreasing lists in order
    # O(n)
    ans = MergeListsInorder(increasing=increasing, decreasing=decreasing)
    return ans

def IncreasingList(A: List[int], Y: int) -> List[int]:
    increasing: List[int] = []
    l, r, count = 0, 0, 0
    while(r < len(A)-Y):
        if A[r] + 1 == A[r+1]:
            r += 1
            count += 1
            if(count == Y-1):
                # ans.append(l)
                increasing.append(l)
                count -= 1
                l += 1
        else:
            r += 1
            l = r
            count = 0
    return increasing

def DecreasingList(A: List[int], Y: int) -> List[int]:
    decreasing: List[int] = []
    l, r, count = 0, 0, 0
    while(r < len(A)-Y):
        if A[r] - 1 == A[r+1]:
            r += 1
            count += 1
            if(count == Y-1):
                # ans.append(l)
                decreasing.append(l)
                count -= 1
                l += 1
        else:
            r += 1
            l = r
            count = 0
    return decreasing

def MergeListsInorder(increasing: List[int], decreasing:List[int]) -> List[int]:
    ans: List[int] = []
    l,r = 0,0
    while(l < len(increasing) and r < len(decreasing)):
        if(increasing[l] < decreasing[r]):
            ans.append(increasing[l])
            l += 1
        else:
            ans.append(decreasing[r])
            r += 1

    if(l == len(increasing)-1):
        ans.extend(decreasing[r:])
    else:
        ans.extend(increasing[l:])
    
    return ans



values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7,8,7]
run_length=3
ans = solution(values, run_length)
print(ans)

values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7,8,7]
run_length=2
ans = solution(values, run_length)
print(ans)




