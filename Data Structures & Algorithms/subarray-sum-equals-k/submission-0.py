class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_freq = {0: 1}
        cur_sum = 0
        count = 0
        for each in nums:
            cur_sum += each
            needed = cur_sum - k
            count += prefix_freq.get(needed, 0)
            prefix_freq[cur_sum] = prefix_freq.get(cur_sum, 0) + 1
        return count
        