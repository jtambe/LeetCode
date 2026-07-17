class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {} # {num: [idx1, idx2, ...]}
        
        for idx, num in enumerate(nums):
            if num in mapping:
                mapping[num].append(idx)
                arr = mapping[num]
                if arr[-1] - arr[-2] <= k:
                    return True
            else:
                mapping[num] = [idx]
                
        return False
                 
        
