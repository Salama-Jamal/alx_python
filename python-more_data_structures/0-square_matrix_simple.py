



#Write a function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        array = []
        for num in arr:
            array.append(num ** 2)
        new_matrix.append(array)
    return new_matrix