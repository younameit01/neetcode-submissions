class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, each in enumerate(nums):
            remain = target - each
            if remain in seen:
                return [seen[remain], index]
            else:
                seen[each] = index