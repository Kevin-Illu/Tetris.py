import numpy as np

A = [[1, 2], [3, 4]]
matriz = np.array(A)

current_matriz = None

for i in range(5):
    if current_matriz is None:
        current_matriz = matriz
    else:
        current_matriz = np.rot90(current_matriz, k=-1)
        
    print(current_matriz[0])
    print(current_matriz[1])
    print()
