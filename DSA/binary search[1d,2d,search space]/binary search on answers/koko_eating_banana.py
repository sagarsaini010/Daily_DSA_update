import math

def find_max(arr):
    n = len(arr)
    maxi = -10**4
    for i in range(n):
        maxi = max(maxi,arr[i])
    return maxi

def totalHourTaken(arr,hourly):
    n= len(arr)
    totalH = 0
    for i in range(n):
        totalH += math.ceil(arr[i]/hourly)
    return totalH

def minimuBananaAtOneTime(arr,hour):
    n = len(arr)
    low = 0
    high = find_max(arr)
    ans = 10**4
    while low <= high:
        mid = (low + high) // 2
        total_h =totalHourTaken(arr,mid)
        if total_h <= hour:
            high = mid-1
        else:
            low = mid+1
    return low


piles = [3,6,7,11]
h = 8
ans = minimuBananaAtOneTime(piles,h)
print(ans)