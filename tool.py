import random
from math import log

import numpy as np


def generate_dataset(table_prob, size):
    dataset = []
    comb = table_prob[0]
    prob = table_prob[1]
    return np.array(random.choices(comb, prob, k=size)).astype(int)


def calculate_binary_value(elem):
    value = 0
    for indx, e in enumerate(elem):
        value = value + e * 2 ** indx
    return value


def kullback_leibler_divergence(distribuction_p, distribuction_qn):
    # distribuction_p: distribuzione del modello da apprendere
    # distribuction_qn:distribuzione del modello appreso dal training set di dimensione n
    result = 0
    i = 0
    while i < len(distribuction_p):
        if distribuction_p[1][i] != 0 and distribuction_qn[1][i] != 0:
            if (distribuction_p[1][i] / distribuction_qn[1][i]) != 0:
                result = result + distribuction_p[1][i] * log(distribuction_p[1][i] / distribuction_qn[1][i], 2)
        i = i + 1
    return result
