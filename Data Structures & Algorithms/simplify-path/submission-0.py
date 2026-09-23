class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for each in path.split("/"):
            if each == "" or each == ".":
                continue
            elif each == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(each)
        return "/" + "/".join(stack)