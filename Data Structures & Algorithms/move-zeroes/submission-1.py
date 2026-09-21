class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers
        # write = 0
        # for each in nums:
        #     if each != 0:
        #         nums[write] = each
        #         write += 1
        
        # while write < len(nums):
        #     nums[write] = 0
        #     write += 1
        # return nums

        # two pointers with swap
        write = 0
        for index, each in enumerate(nums):
            if each != 0:
                nums[write], nums[index] = nums[index], nums[write]
                write += 1
        return nums                