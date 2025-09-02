def search_in_matrix(matrix,k):
    n = len(matrix)
    m = len(matrix[0])
    row =0
    col = m-1
    while row < n and col >=0:
        if matrix[row][col] == k:
            return True
        elif matrix[row][col] <  k:
            row +=1
        else:
            col +=1