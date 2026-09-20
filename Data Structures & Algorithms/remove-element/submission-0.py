class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for each in nums:
            if each != val:
                nums[write] = each
                write += 1
        return write