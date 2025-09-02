def merge(intervals):
    n = len(intervals)
    ans =[]
    intervals.sort()

    # for i in range(n):
    #     start,end = intervals[i][0],intervals[i][1]

    #     if ans and end <= ans [-1][1]:
    #         continue
    #     for j in range(i+1,n):
    #         if intervals[j][0]<=end:
    #             end = max(end,intervals[j][1])
    #         else:
    #             break
    #     ans.append([start,end])

    for i in range(n):
        if not ans or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1],intervals[i][1])
            
    return ans

arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
ans = merge(arr)
print(ans)




# from typing import List

# def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
#     n = len(arr) # size of the array

#     # sort the given intervals:
#     arr.sort()

#     ans = []

#     for i in range(n): # select an interval:
#         start, end = arr[i][0], arr[i][1]

#         # Skip all the merged intervals:
#         if ans and end <= ans[-1][1]:
#             continue

#         # check the rest of the intervals:
#         for j in range(i + 1, n):
#             if arr[j][0] <= end:
#                 end = max(end, arr[j][1])
#             else:
#                 break
#         ans.append([start, end])
#     return ans

# if __name__ == '__main__':
#     arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
#     ans = mergeOverlappingIntervals(arr)
#     print("The merged intervals are:")
#     for it in ans:
#         print(f"[{it[0]}, {it[1]}]", end=" ")
#     print()



