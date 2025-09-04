<<<<<<< HEAD
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check_dict = {}
        n = len(s)
        for i in range(n):
            if s[i]  in check_dict and check_dict[s[i]] == t[i]:
                pass
            elif s[i] not in check_dict and t[i] not in check_dict.values():
                check_dict[s[i]] = t[i]
            else:
                return False
        return True
=======
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check_dict = {}
        n = len(s)
        for i in range(n):
            if s[i]  in check_dict and check_dict[s[i]] == t[i]:
                pass
            elif s[i] not in check_dict and t[i] not in check_dict.values():
                check_dict[s[i]] = t[i]
            else:
                return False
        return True
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
            