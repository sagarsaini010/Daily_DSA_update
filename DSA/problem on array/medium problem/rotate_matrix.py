def rotate_matrix(matrix,n):
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_matrix(arr,3)
    print("Rotated Image")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
