def sumd(matrix):
    dsum = 0
    for i in range(len(matrix)):
        dsum += matrix[i][i]
    return dsum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

res = sumd(matrix)
print(res)