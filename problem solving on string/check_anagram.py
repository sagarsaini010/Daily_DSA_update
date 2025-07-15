class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check_dict ={}
        # n = len(s)
        # m = len(t)
        # if n != m:
        #     return False
        # s_s = list(s)
        # t_t = list(t)
        # for i in range(n):
        #     check_dict[s_s[i]] = check_dict.get(s_s[i],0)+1
        # for j in range(n):
        #      check_dict[t_t[j]] = check_dict.get(t_t[j],0)-1
        # if all(value == 0 for value in check_dict.values()):
        #     return True
        # else:
        #     return False


        # if len(s) != len(t):
        #     return False
        # count = [0]*26
        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')]+=1
        #     count[ord(t[i]) - ord('a')]-=1
        # return all(c == 0 for c in count)


        for ch in set(s):
            if s.count(ch) != t.count(ch) or len(s) != len(t):
                return False
        return True