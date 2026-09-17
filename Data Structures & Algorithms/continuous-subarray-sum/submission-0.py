class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0: -1}
        cur_sum = 0

        for right, each in enumerate(nums):
            cur_sum += each
            remainder = cur_sum % k
            if remainder in remainder_index:
                length = right - remainder_index[remainder]
                if length >= 2:
                    return True
            else:
                remainder_index[remainder] = right
        return False
        