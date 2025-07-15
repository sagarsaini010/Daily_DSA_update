class Solution:
    def strStr(self, haystack: str, needle: str) -> int:    
        i = haystack.find(needle)
        if i == -1:
            return i
        else:
            return i