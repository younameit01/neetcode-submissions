class Solution:
    def isValid(self, s: str) -> bool:
        matching = {")": "(", "}": "{", "]": "["}
        results = []

        for each in s:
            if each in ["(", "{", "["]:
                results.append(each)
            else:
                if not results:
                    return False
                if matching[each] != results[-1]:
                    return False
                results.pop()
        return len(results) == 0