class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[": 
                stack.append(i)

            elif i in ")}]":
                if len(stack) == 0: 
                    return False 
                open_side = stack.pop()
                if (i == ")" and open_side != "(") or (i == "}" and open_side != "{") or (i == "]" and open_side != "["): return False 
        if len(stack) == 0:
            return True

        return False