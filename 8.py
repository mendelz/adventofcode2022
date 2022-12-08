import numpy as np
test = """30373
25512
65332
33549
35390"""

def create_matrix(inputstring):
    rows = []
    for thing in inputstring.split():
        row = []
        for item in thing: 
            row.append(item)  
        rows.append(row)

    return np.array(rows), len(inputstring.split()), len(inputstring.split()[0])

matrix, column_length, row_length = create_matrix(test)
print(matrix)
print(column_length)
print(row_length)
# print(matrix)

# for rowidx, row in enumerate(matrix):
#     print(row, rowidx)
#     for colidx, col in enumerate(row):
#         print(col, colidx)
#         print(matrix[rowidx])
print(matrix[0, :])
print(matrix[:, 0])