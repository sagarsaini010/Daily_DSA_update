def pascal_triangle(n):
    ans=[]
    for i in range(n):
        ellement_arr=[]
        sum =0
        for j in range(i+1):
            if j == 0 or j==i:
                ellement_arr.append(1)
            else:
                sum = ans[i-1][j-1]+ans[i-1][j]
                ellement_arr.append(sum)
        ans.append(ellement_arr)
    return ans


ans = pascal_triangle(1)
print(ans)
