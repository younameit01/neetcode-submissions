class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for each in nums:
            if each != nums[write - 1]:
                nums[write] = each
                write += 1
        return write