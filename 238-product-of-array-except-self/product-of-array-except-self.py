class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # First pass: fill in left products
        for i in range(1,n):
            answer[i] = answer[i-1] * nums[i-1]

        # Second pass: multiply with right products on the fly
        right = 1
        for i in range(n-1,-1,-1):
            answer[i] *= right
            right *= nums[i]

        return answer
        # Two pass approach and TC:O(N),SC:O(1) or O(N)