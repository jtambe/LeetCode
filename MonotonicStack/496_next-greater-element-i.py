
# https://www.youtube.com/watch?v=8BDKB2yuGyg
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        next_greater = {} # {num : next greater number}
        stack = [] # monotonic stack
        ans = [-1 for i in range(len(nums1))]

        # build next_greater dictionary from nums2
        for num2 in nums2:
            while (any(stack) and stack[-1] <= num2): # after 1st, check if added number was less than current
                num = stack.pop()
                next_greater[num] = num2 # if added number was less than current, then we have dictionary data

            stack.append(num2) # 1st add current number in stack

        # Finally use the dictionary to create result
        for i in range(len(nums1)):
            if nums1[i] in next_greater:
                ans[i] = next_greater[nums1[i]]

        return ans


    
    def nextGreaterElement_similar_solution_as_503(self, nums1: List[int], nums2: List[int]) -> List[int]:

        monotonic_stack = []
        dictionary = {item:-1 for item in nums1}

        for i in range(len(nums2)-1, -1, -1):

            while monotonic_stack and monotonic_stack[-1] <= nums2[i]:
                monotonic_stack.pop()

            if nums2[i] in dictionary:
                if monotonic_stack and monotonic_stack[-1] > nums2[i]:
                    dictionary[nums2[i]] = monotonic_stack[-1]
                if not monotonic_stack:
                    dictionary[nums2[i]] = -1

            monotonic_stack.append(nums2[i])

        return list(dictionary.values())




        # ans = [-1 for i in range(len(nums1))]

        # d = {}
        # for i in range(len(nums2)):
        #     d[nums2[i]] = i

        # for i in range(len(nums1)):
        #     idx = d[nums1[i]]
        #     while(idx < len(nums2)):
        #         if nums2[idx] > nums1[i]:
        #             ans[i] = nums2[idx]
        #             break
        #         idx += 1

        # return ans
        
