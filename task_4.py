def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]

n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))
mat = []
for i in range(n):
    row = list(map(int, input(f"Введите {i+1}-ю строку ({m} чисел через пробел): ").split()))
    mat.append(row)
print("Транспонированная матрица:")
for r in transpose(mat):
    print(r)
