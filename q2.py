import numpy as np

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    max_score = 0
    L = np.zeros((m + 1, n + 1))

    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = 0
            if L[i][j] > max_score:
                max_score = L[i][j]

    return max_score

S, T = 'TAGTCACG', 'AGACTGTC'

print("Length of LCS is ", lcs(S, T))