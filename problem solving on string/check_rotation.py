class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # n = len(goal)
        # m = len(s)
        # s_s = list(s)
        # g_goal = list(goal)
        # if m != n:
        #     return False
        
        # for i in range(n):
        #     temp = s_s[0]
        #     for j in range(n-1):
        #         if s_s == g_goal:
        #             return True
        #         else:
        #             s_s[j] = s_s[j+1]
        #     s_s[n-1] = temp
        # return False
        return len(s) == len(goal) and goal in (s+s)