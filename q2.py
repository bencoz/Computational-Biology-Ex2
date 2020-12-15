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


MAX = 11


# Return LCS with at most 2 changes allowed.
def lcs_at_most_2_mismatches(X, Y):
    m = len(X)
    n = len(Y)
    max_score = 0
    L0 = np.zeros((m + 1, n + 1))
    L1 = np.zeros((m + 1, n + 1))
    L2 = np.zeros((m + 1, n + 1))

    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                L0[i][j] = L0[i - 1][j - 1] + 1
            else:
                L0[i][j] = 0
            if L0[i][j] > max_score:
                max_score = L0[i][j]

    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                L1[i][j] = L1[i - 1][j - 1] + 1
            else:
                L1[i][j] = L0[i - 1][j - 1] + 1
            if L1[i][j] > max_score:
                max_score = L1[i][j]

    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                L2[i][j] = L2[i - 1][j - 1] + 1
            else:
                L2[i][j] = L1[i - 1][j - 1] + 1
            if L2[i][j] > max_score:
                max_score = L2[i][j]

    return max_score


S, T = 'AATTAAAAGCC', 'AACCAAAATCC'
# print("Length of LCS is ", lcs(S, T))

score = lcs_at_most_2_mismatches(S, T)
print("Length of LCS with 2 changes is ", score)
