class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        idx = 0
        while idx < n:
            l, r = idx+1, n-1
            while l <= r:
                mid = (l+r)//2
                if target == numbers[idx] + numbers[mid]:
                    return [idx+1, mid+1]
                elif target < numbers[idx] + numbers[mid]:
                    r = mid-1
                elif target > numbers[idx] + numbers[mid]:
                    l = mid+1
            idx += 1
