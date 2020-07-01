from math import log

import pyBN
from pyBN import *
import numpy as np
from matplotlib.pyplot import ylabel, plot, show, xlabel
from itertools import product


def update_cpt(node):
    total = []
    len_par = int(2 ** len(node["parents"]))
    num = int(len(node["counts"]) / len_par)
    for i in range(0, len_par):
        total.append(sum(node["counts"][0 + num * i:num + num * i]))
    j = 0
    for i in node["counts"]:
        node["cpt"][j] = round(i / total[int(j / num)], 2)
        j += 1


def add_bn_hyperparameter(bn, hyper):
    for i in bn.V:
        bn.F[i]["counts"] = np.full(2 ** (len(bn.F[i]["parents"]) + 1), hyper, dtype=int)


def calculate_binary_value(elem):
    value = 0
    for indx, e in enumerate(elem):
        value = value + e * 2 ** indx
    return value


def update_counts_of_node(node, data):
    unique, counts = np.unique(data, return_counts=True, axis=1)
    ind = 0
    for i in unique.T:
        for j in range(0, len(i)):
            i[j] = 1 - i[j]
        num = (2 ** (len(node["parents"]) + 1)) - calculate_binary_value(i) - 1
        node["counts"][num] = node["counts"][num] + counts[ind]
        ind = ind + 1


def update_counts_of_bn(training_set, bn):
    ind_calc = []
    for i in bn.V:
        ind_calc.append(training_set[:, bn.node_idx(i)])
        parents = bn.F[i]['parents']
        for p in parents:
            ind_calc.append(training_set[:, bn.node_idx(p)])
        update_counts_of_node(bn.F[i], ind_calc)
        ind_calc.clear()


def get_value_of_cpt(node, index_of_element):
    index_of_element = list(map(int, index_of_element))
    num = (2 ** (len(node["parents"]) + 1)) - calculate_binary_value(index_of_element) - 1
    return node["cpt"][num]


def calculate_probability_distribution_of_bn(bn):
    result = []
    idxcalc = []
    probability = 1
    combination = list(product("01", repeat=len(bn.V)))
    for comb in combination:
        for i in bn.V:
            idxcalc.append(comb[bn.node_idx(i)])
            parents = bn.F[i]['parents']
            for p in parents:
                idxcalc.append(comb[bn.node_idx(p)])
            prob = get_value_of_cpt(bn.F[i], idxcalc)
            probability = probability * prob
            idxcalc.clear()
        result.append(probability)
        probability = 1
    return result


def kullback_leibler_divergence(distribuction_p, distribuction_qn):
    # distribuction_p: distribuzione 'vera'
    # distribuction_qn:distribuzione appresa dal training set di dimensione n
    result = 0
    i = 0

    while i < len(distribuction_p):
        if distribuction_p[i] != 0 and distribuction_qn[i] != 0:
            if (distribuction_p[i] / distribuction_qn[i]) != 0:
                result = result + distribuction_p[i] * log(distribuction_p[i] / distribuction_qn[i], 2)
        i = i + 1
    return result


def main(path_bn='/home/pietro/Documenti/Unifi/IA/pyBN-master/data/asia.bif', hyperparameter=1,
         size_of_training_sets=None, print_bn=False):
    if size_of_training_sets is None:
        size_of_training_sets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 50, 100, 200, 300, 400, 500, 600, 1000, 2000]

    original_bn = read_bn(path_bn)
    working_bn = original_bn.copy()
    add_bn_hyperparameter(working_bn, hyperparameter)
    size_of_training_sets.sort()
    result = []
    training_set = pyBN.random_sample(working_bn, size_of_training_sets[len(size_of_training_sets) - 1])
    prec_training_value = 0
    distribuction_p = calculate_probability_distribution_of_bn(original_bn)

    for current_training_quantity in size_of_training_sets:
        update_counts_of_bn(training_set[prec_training_value:current_training_quantity], working_bn)
        for i in working_bn.V:
            update_cpt(working_bn.F[i])
        distribuction_qn = calculate_probability_distribution_of_bn(working_bn)

        result.append(kullback_leibler_divergence(distribuction_p, distribuction_qn))
        prec_training_value = current_training_quantity
        if print_bn:
            print(working_bn.F)
    if print_bn:
        print(original_bn.F)
    plot(size_of_training_sets, result)
    ylabel("valori della divergenza")
    xlabel("dimensione dataset")
    show()
    


main()
