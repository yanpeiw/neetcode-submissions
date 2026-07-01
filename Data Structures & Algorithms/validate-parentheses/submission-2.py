class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        closingToopen = {")": "(", "]":"[", "}":"{"}

        for c in s:
            if c in closingToopen:
                if ans and ans[-1] == closingToopen[c]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(c)
        return True if not ans else False
            
            


