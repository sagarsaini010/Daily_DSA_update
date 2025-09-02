def mark_row(matrix,n,m,i):
    for j in range(m):
        if matrix[i][j] !=0:
            matrix[i][j]= -1

def mark_col(matrix,n,m,j):
    for i in range(n):
        if matrix[i][j] !=0:
            matrix[i][j] = -1


def set_zeros_in_matrix(matrix):
    n = len(matrix)
    m= len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                mark_row(matrix,n,m,i)
                mark_col(matrix,n,m,j)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix
        

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
ans = set_zeros_in_matrix(matrix)

print("The Final matrix is:")
print(ans)
