class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss=s.strip().split(' ')
        return len(ss[-1])