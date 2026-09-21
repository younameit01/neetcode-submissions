class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        write = len(nums) - 1
        results = [0] * len(nums)

        while left <= right:
            left_squared = nums[left] * nums[left]
            right_squared = nums[right] * nums[right]

            if left_squared > right_squared:
                results[write] = left_squared
                left += 1
            else:
                results[write] = right_squared
                right -= 1
            write -= 1
        return results