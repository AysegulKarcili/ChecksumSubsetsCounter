"""
Given a set of integers, find the number of subsets in which the largest element equals the sum of remaining 2 or more elements.
"""
import numpy as np


def checksum_subsets_counter(input_vec):
    input_vec = np.sort(input_vec)
    input_trunc = input_vec[:-1]
    num_el = len(input_trunc)
    num_prob = 2 ** num_el

    aaa = np.array(range(num_prob))
    selection_mat = np.zeros(shape=(num_prob, num_el), dtype=int)
    for i in range(num_prob):
        for j in range(num_el):
            temp = bin(aaa[i])[2:].zfill(num_el)  # a string of length numel
            selection_mat[i, j] = list(temp)[j]

    sum_row = np.sum(selection_mat, axis=1)
    selection_mat = selection_mat[sum_row != 1, :]  # sum_row being 0 is dummy, can also be discarded
    sums_selected = np.matmul(selection_mat, input_trunc)  # !!!!!

    cnt = 0
    for sm in sums_selected:
        for el in input_vec:
            if sm == el:
                cnt = cnt + 1
                break

    return cnt


if __name__ == '__main__':
    print('###############')
    input_set = [2, 4, 6, 8, 10, 12]
    # input_set = [4, 5, 10, 15, 16, 20, 29, 38, 48, 51, 55, 57, 60, 62, 71, 74, 79, 82, 93, 96, 98, 100, 200]
    num_valid_subsets = checksum_subsets_counter(input_set)
    print(f'num_valid_subsets: {num_valid_subsets}')
    print('###############')
