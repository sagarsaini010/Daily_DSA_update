def longest_consecutive_sequence(arr):
    n = len(arr)
    # arr.sort()
    count = 0
    longest =1
    st = set()
    for i in range(n):
        st.add(arr[i])

    for it in st:
        if it-1 not in st:
            count = 1
            x =it
            while x+1 in st:
                x+=1
                count+=1
            longest = max( longest , count)
    return longest

    # for i in range(n):
    #     if arr[i]-1 == last_smaller:
    #         count+=1
    #         last_smaller = arr[i]
    #     elif arr[i] == last_smaller:
    #         pass
    #     elif arr[i] != last_smaller:
    #         count=1
    #         last_smaller = arr[i]

    #     longest = max(longest,count)
    # return longest

arr = [1,2,3,4,54,53,52,5,6]
ans = longest_consecutive_sequence(arr)
print(ans) 