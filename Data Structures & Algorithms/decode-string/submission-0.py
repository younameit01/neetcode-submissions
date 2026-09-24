class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0

        for each in s:
            if each.isdigit():
                cur_num = cur_num * 10 + int(each)
            elif each == "[":
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif each == "]":
                prev_str, count = stack.pop()
                cur_str = prev_str + cur_str * count
            else:
                cur_str += each
        return cur_str