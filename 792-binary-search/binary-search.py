class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m]>target:
                r = m - 1
            elif nums[m]<target:
                l = m+1
        return -1         
                
# TC:O(logn),because n/2,n/4,n/8..n/2^k, k = log(n)
# SC:O(1), no extra space is used

