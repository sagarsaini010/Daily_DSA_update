class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        days = max(bloomDay)

        while low <= high:
            mid = (low+high)//2

            bouquet = 0
            flower =0
            for i in bloomDay:
                if i <= mid:
                    flower +=1
                    if flower/k == 1:
                        bouquet +=1
                        flower =0
                elif i > mid:
                    flower =0
                
            if bouquet >= m:
                days = mid
                high = mid-1
            else:
                low = mid+1
        return days
