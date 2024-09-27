## Simple determinant calculator (I learned the recursive formula for a determinant and decided to code it up)
## Yes I know that numpy can do this but I want to implement it myself

import numpy as np ## for easier matrix manipulation

def determinant(matrix): ## matrix is any n x n matrix 

    ## Processing and checking the input to make sure it has the right type, shape, etc (boring)

    if type(matrix) != np.array: ## turn the array into a numpy array if necessary
        matrix = np.array(matrix)

    if len(matrix.shape) != 2:
        raise ValueError("Matrix is not 2D") ## matrix must be 2D to have
    elif matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix is not square") ## matrix must be square to have a determinant
    
    ## Now the real fun part
    
    ## base case
    if matrix.shape[0] == 2: ## both will be 2 since it is a square matrix
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    else:
        det = 0
        for i in range(len(matrix)): ## iterate over all of the columns
            new_matrix_no_first_row = np.delete(matrix, (0), axis=0) ## Removes the first row from the matrix
            new_matrix_no_ith_column = np.delete(new_matrix_no_first_row, (i), axis=1) ## Removes the ith column from the matrix
            to_add = matrix[0,i] * determinant(new_matrix_no_ith_column) ## shitty variable name

            if i % 2 == 1: ## Determines the sign of value at (i, j)
                det += to_add
            else:
                det -= to_add

        return det ## this code doesnt work




mat = [[1, 2, 3, 4], [1, 0, 2, 0], [0, 1, 2, 3], [2, 3, 0, 0]]
print(determinant(mat))
mat = np.array(mat)
print(np.linalg.det(mat))
mat = [[1, 2, 4], [2, 1, -3], [4, 0, 1]]
print(determinant(mat))
mat = np.array(mat)
print(np.linalg.det(mat))
mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5]]
print(determinant(mat))
mat = np.array(mat)
print(np.linalg.det(mat))