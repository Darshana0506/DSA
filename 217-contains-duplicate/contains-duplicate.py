from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count  = Counter(nums)
        for i,n in count.items():
            if n>1:
                return True
        return False
        # hashmap or frequency method
        # TC,SC:O(N)