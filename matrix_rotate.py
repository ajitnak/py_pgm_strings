def matrix_rotate(matrix):
    #reset the coulmn and row t zero if one element is zero
    rows = len(matrix)
    cols = len(matrix[0])

	if rows == 0 or rows != cols:
		return False

	for layer in range(rows/2):  # outer loop for going over half rows, shrinking squares
		first = layer
		last = rows - 1 - layer
		for i in range(first, last): #inner loop for swapping indidual elements
			offset = i - first
			top = matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] =  matrix[last][last-offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = top

	return True
