def spiral_matrix(matrix,n):
    top=0
    left=0
    right=n-1
    bottom =n-1
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            print(matrix[top][i])
        top+=1
        for j in range(top,bottom+1):
            print(matrix[j][right])
        right-=1
        if top<=bottom:
            for k in range(right,left-1,-1):
                print(matrix[bottom][k])
            bottom-=1
        if left<=right:
            for l in range(bottom,top-1,-1):
                print(matrix[l][left])
            left+=1

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
spiral_matrix(mat,4)