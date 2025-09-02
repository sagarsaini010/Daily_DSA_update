def rotate_matrix(matrix,n):
    new_matrix= [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[j][n-1-i]=matrix[i][j]
    return new_matrix

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = rotate_matrix(arr,3)
print("Rotated Image")
for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            print(rotated[i][j], end=" ")
        print()