<<<<<<< HEAD
class Solution:
    def maxDepth(self, s: str) -> int:
        max_n = 0
        count =0
        n = len(s)
        for ch in s:
            if ch == '(':
                count += 1
                max_n = max(max_n,count)
            elif ch == ')':
                count -= 1
        return max_n
=======
class Solution:
    def maxDepth(self, s: str) -> int:
        max_n = 0
        count =0
        n = len(s)
        for ch in s:
            if ch == '(':
                count += 1
                max_n = max(max_n,count)
            elif ch == ')':
                count -= 1
        return max_n
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
