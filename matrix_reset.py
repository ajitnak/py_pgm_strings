def matrix_reset_rows_cols(matrix):
    #reset the coulmn and row to zero if one element is zero
    rows = len(matrix)
    cols = len(matrix[0])

    col_one_has_zero = False
    row_one_has_zero = False

    for i in range(rows):
        if matrix[i][0] == 0:
            col_one_has_zero = True
            break

    for i in range(cols):
        if matrix[0][i] == 0:
            row_one_has_zero = True
            break

    for i in range(1, rows):
        for j in rangeI(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    for i in range(1, cols):
        if matrix[0][i] == 0:
            nullify_col(matrix, i)

    if col_one_has_zero:
        nullify_col(matrix, 0)
        
    if row_one_has_zero:
        nullify_row(matrix, 0)

def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
            
            
