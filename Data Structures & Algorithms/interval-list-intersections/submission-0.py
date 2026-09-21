class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        results = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            overlap_start = max(start1, start2)
            overlap_end = min(end1, end2)

            if overlap_start <= overlap_end:
                results.append([overlap_start, overlap_end])
            
            if end1 < end2:
                i += 1
            else:
                j += 1
        return results