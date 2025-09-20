matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_a = [
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
]

matrix_o = [
    [111, 2222, 333],
    [4, 5, 6],
    [7, 8, 9]
    ]

dict_mat = {
    "matrix": matrix,
    "matrixA": matrix_a,
    "matrixO": matrix_o
}

def print_matrix_a(dict_arg):
    second_mat = list(dict_arg.values())[1]
    for inner_mat in second_mat:
        for item in inner_mat:
            print(item)


print_matrix_a(dict_mat)