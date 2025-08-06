from collections import deque
def nextSmallerElements(arr):
    # Your code goes here
    nge=[]
    n = len(arr)
    st = deque()
    for i in range(n-1,-1,-1):
        while len(st)!=0 and arr[i] <= st[-1]:
            st.pop()
        nge.append(-1 if len(st) == 0 else st[-1])
        st.append(arr[i])

    return list(reversed(nge))




arr = [4, 8, 5, 2, 25]

print(nextSmallerElements(arr))