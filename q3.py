import numpy as np


def sum_homology(S, T):
    p_match = 32 / 160
    p_mismatch = 2 / 160
    p_indel = 1 / 160

    arr_first = np.zeros(min(len(T) + 1, len(S) + 1), dtype=float)
    arr_second = np.zeros(min(len(T) + 1, len(S) + 1), dtype=float)

    arr_first[0] = 1

    if len(S) < len(T):
        temp = S
        S = T
        T = temp

    for idx_S in range(1, len(S) + 1):
        for idx_T in range(1, len(T) + 1):
            arr_second[idx_T] = sum([arr_first[idx_T - 1] * (p_match if S[idx_S - 1] == T[idx_T - 1] else p_mismatch), \
                                     arr_second[idx_T - 1] * p_indel, \
                                     arr_first[idx_T] * p_indel])
        arr_first = arr_second.copy()
        arr_second = np.zeros(len(T) + 1, dtype=float)
    return arr_first[-1]


def NW_from_hw1(a, b, match_score=2, gap_cost=-3, mismatch_score=-2):
    H = np.ones((len(a) + 1, len(b) + 1), np.int) * (-np.inf)

    for i in range(0, H.shape[0]):
        for j in range(0, H.shape[1]):
            if i == 0 and j == 0:
                H[i, j] = 0.0
            elif i == 0 and j != 0:
                H[i, j] = H[i, j - 1] + gap_cost
            elif j == 0 and i != 0:
                H[i, j] = H[i - 1, j] + gap_cost
            else:
                H[i, j] = max(H[i - 1, j - 1] + (match_score if a[i - 1] == b[j - 1] else mismatch_score), \
                              H[i, j - 1] + gap_cost, \
                              H[i - 1, j] + gap_cost)
    return H[-1, -1]


def find_max_n(S, T):
    x = sum_homology(S, T)
    n = 0
    while x != 0:
        n += 1
        S = 'T' + S
        x = sum_homology(S, T)
    return [n, S]


S, T = 'ATAAGGCATTGACCGTATTGCCAA', 'CCCATAGGTGCGGTAGCC'

print("The sumHomology is: ", sum_homology(S, T))

n = find_max_n(S, T)[0]
new_S = find_max_n(S, T)[1]

print("The number of T's added until probability is 0 is: ", n)
print("The score of the global alignment from hw 1 with the new sequence is: ", NW_from_hw1(new_S, T))
