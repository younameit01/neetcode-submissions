class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for each in nums:
            if count == 0:
                candidate = each
            
            if each == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        