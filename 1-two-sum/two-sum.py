class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i,n in enumerate(nums):
            # {0:2,1:7,2:11,3:15}
            diff = target - n
            if diff in hashSet:
                return [i,hashSet[diff]]
            else:
                hashSet[n] = i
                # HashMap Approach
                # TC:O(N),SC:O(N)