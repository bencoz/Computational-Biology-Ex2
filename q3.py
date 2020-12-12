import itertools
import numpy as np
import math

""" Question 3 b"""


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    max_score = 0
    # declaring the array for storing the dp values
    L = np.zeros((m + 1, n + 1))

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = 0
            if L[i][j] > max_score:
                max_score = L[i][j]

    return max_score


def sum_homology(S, T):
    p_match = 0.2
    p_mismatch = 0.0125
    p_indel = 0.00625

    arr_first = np.empty(len(T) + 1, dtype=float)
    arr_second = np.empty(len(T) + 1, dtype=float)

    arr_first[0] = 0.0

    for x in range(1, len(arr_first)):
        arr_first[x] = arr_first[x - 1] + math.log(p_indel)*-1

    for idx_S in range(1, len(S) + 1):
        for idx_T in range(len(T) + 1):
            if (idx_T == 0):
                arr_second[idx_T] = arr_first[idx_T] + math.log(p_indel)*-1
            else:
                if (S[idx_S - 1] == T[idx_T - 1]):
                    misORmatchProb = arr_first[idx_T - 1] + math.log(p_match)*-1
                else:
                    misORmatchProb = arr_first[idx_T - 1] + math.log(p_mismatch)*-1

                arr_second[idx_T] = sum([misORmatchProb,
                                         arr_second[idx_T - 1] + math.log(p_indel)*-1,
                                         arr_first[idx_T] + math.log(p_indel)*-1])

        # print("First array: ", arr_first)

        arr_first = arr_second
        arr_second = np.empty(len(T) + 1, dtype=float)

    print("\nThe sumHomology is: ", arr_first[-1])


S, T = 'ATAAGGCATTGACCGTATTGCCAA', 'CCCATAGGTGCGGTAGCC'

sum_homology(S, T)

S, T = 'TAGTCACG', 'AGACTGTC'

print("Length of LCS is ", lcs(S, T))
