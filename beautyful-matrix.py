matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

row_distance = 0
col_distance = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_distance = abs(i - 2)
            col_distance = abs(j - 2)

moves_required = row_distance + col_distance
print(moves_required)
