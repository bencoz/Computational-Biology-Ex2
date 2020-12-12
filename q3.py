import itertools
import numpy as np
import math

""" Question 3 b"""
def sum_homology(S, T):
    p_match = 0.2
    p_mismatch = 0.0125
    p_indel = 0.00625

    arr_first = np.empty(len(T) + 1, dtype=float)
    arr_second = np.empty(len(T) + 1, dtype=float)

    arr_first[0] = 1

    for x in range(1, len(arr_first)):
        arr_first[x] = arr_first[x - 1] * p_indel #math.log(p_indel)*-1

    for idx_S in range(1, len(S) + 1):
        for idx_T in range(len(T) + 1):
            if (idx_T == 0):
                arr_second[idx_T] = arr_first[idx_T] * p_indel #math.log(p_indel)*-1
            else:
                if (S[idx_S - 1] == T[idx_T - 1]):
                    misORmatchProb = arr_first[idx_T - 1] * p_match #math.log(p_match)*-1
                else:
                    misORmatchProb = arr_first[idx_T - 1] * p_mismatch #math.log(p_mismatch)*-1

                arr_second[idx_T] = sum([misORmatchProb,
                                         arr_second[idx_T - 1] * p_indel, #math.log(p_indel)*-1,
                                         arr_first[idx_T] * p_indel]) #math.log(p_indel)*-1])

        # print("First array: ", arr_first)

        arr_first = arr_second.copy()
        arr_second = np.empty(len(T) + 1, dtype=float)

    print("\nThe sumHomology is: ", arr_first[-1])


S, T = 'ATAAGGCATTGACCGTATTGCCAA', 'CCCATAGGTGCGGTAGCC'

sum_homology(S, T)


