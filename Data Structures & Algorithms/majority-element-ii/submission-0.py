class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for each in nums:
            if each == candidate1:
                count1 += 1
            elif each == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = each
                count1 += 1
            elif count2 == 0:
                candidate2 = each
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for each in nums:
            if each == candidate1:
                count1 += 1
            elif each == candidate2:
                count2 += 1
        
        result = []
        if count1 > len(nums)//3:
            result.append(candidate1)
        if count2 > len(nums)//3 and candidate2 != candidate1:
            result.append(candidate2)
        
        return result