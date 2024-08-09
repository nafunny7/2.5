def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(4, 9, 10)
res1 = get_matrix(12, 3, 45)
print(res1)
print(result1)

