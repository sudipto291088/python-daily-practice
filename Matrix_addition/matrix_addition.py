matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8, 9],
    [1, 2, 3]
]

result = []

for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Resultant Matrix:")

for r in result:
    print(r)





Resultant Matrix:
[8, 10, 12]
[5, 7, 9]