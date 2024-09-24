def det(A, n):
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] *  A[1][0]
    elif n == 3:
        plus = A[0][0] * A[1][1] * A[2][2] + A[1][0] * A[0][2] * A[2][1] + A[2][0] * A[0][1] * A[1][2]
        minus = A[2][0] * A[1][1] * A[0][2] + A[0][0] * A[2][1] * A[1][2] + A[1][0] * A[0][1] * A[2][2]
        return plus - minus
    else:
        return 'bad input'
def replace(A, b, n, ind):
    #ind - индекс столбца вместо которого ставится столбец b
    Acopy = [row[:] for row in A]
    for i in range(n):
        Acopy[i][ind] = b[i]
    return Acopy

def cramer(A, b, n):
    '''
    :param A: матрица (двумерный массив) n x n
    :param b: столбец свободных значений
    :param n: размер матрицы
    :return: список из значений переменных
    '''
    res = []
    D = det(A, n)
    for ind in range(n):
        Di = det(replace(A, b, n, ind), n)
        res.append(Di / D)
    return res

#2 на 2
A = [[2, 3], [4, -5]]
b = [1, 1]
print(*cramer(A, b, 2))
# 3 на 3
A = [[3, -1, 2], [1, 4, -1], [2, 3, 1]]
b = [-4, 10, 8]
print(*cramer(A, b, 3))