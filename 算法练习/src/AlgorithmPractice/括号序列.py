class Solution:
    def isValid(self, s):
        # write code here
        s = list(s)
        s.reverse()
        res = []
        for t in range(len(s)):
            if s[-1] == '(' or s[-1] == '[':
                res.append(s.pop())
            else:
                if len(res) == 0:
                    return False
                if s[-1] == ')':
                    if len(res) == 0:
                        return False
                    if res[-1] == '(':
                        res.pop()
                        s.pop()
                    else:
                        return False
                if s[-1] == ']':
                    if len(res) == 0:
                        return False
                    if res[-1] == '[':
                        res.pop()
                        s.pop()
                    else:
                        return False

        if len(res) == 0:
            return True


sol = Solution()
print(sol.isValid(input()))