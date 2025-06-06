m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

trans = [[0, 0, 0],
         [0, 0, 0],
         [0, 0 ,0]]

for i in range(3):
    for j in range(3):
        trans[j][i] = m[i][j]

        for linha in range(3):
            for coluna in range(3):
                print('%4d' % trans{linha}[coluna], end = '')
        print()

m_trans = list(map(list, zip(*m)))
for linha in range(3):
    for coluna in range(3):
        print('%4d' % m_trans[linha][coluna], end = '')
    print()    











