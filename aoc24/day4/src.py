import sys

with open(sys.argv[1],'r') as f:
    puzzle = [line.rstrip() for line in f]

R = len(puzzle)
C = len(puzzle[0])

def x_mas(square):
    diag1 = square[0][0] + square[1][1] + square[2][2]
    diag2 = square[0][2] + square[1][1] + square[2][0] 
    return (diag1 in ['MAS', 'SAM']) and (diag2 in ['MAS','SAM'])

def get_rows_cols_diags(i, j):
    row = puzzle[i][j:j+4] if j + 4 <= C else ''
    col = ''.join(puzzle[k][j] for k in range(i, i+4) if k < R) if i + 4 <=R  else ''
    diag_dec = ''.join(puzzle[i+k][j+k] for k in range(4) if i+k <R and j+k < C)
    diag_inc = ''.join(puzzle[i-k][j+k] for k in range(4) if i-k >= 0 and j+k < C)
    
    return [row, row[::-1], col, col[::-1], diag_inc, diag_inc[::-1], diag_dec, diag_dec[::-1]]

s1 = s2 =  0
for i in range(len(puzzle)):
    for j in range(len(puzzle)):
        s1 += sum([line == 'XMAS' for line in get_rows_cols_diags(i,j)])
        if i<R-2 and j < C-2:
            sub = [puzzle[k][j:j+3] for k in range(i,i+3)]
            s2+=x_mas(sub)
print(s1,s2)