from math import log


import numpy as np
import matplotlib.pyplot as plt
from pyBN.io.read import read_bn
from pyBN.utils.random_sample import random_sample


def calculatePosteriorMarginalization(node):
    total = []
    lenPar = int(2 ** len(node["parents"]))
    num = int(len(node["counts"]) / lenPar)
    for i in range(0, lenPar):
        total.append(sum(node["counts"][0 + num * i:num + num * i]))
    j = 0
    for i in node["counts"]:
        node["cpt"][j] = round(i / total[int(j / num)], 2)
        j += 1


def addBNHyperparameter(bn, hyper):
    # Aggiunge ai nodi definiti all'interno di bn, un contatore per tutte le possibili
    # combinazione dei valori del dominio dei genitori del nodo
    for i in bn.V:
        bn.F[i]["counts"] = np.full(2 ** (len(bn.F[i]["parents"]) + 1), hyper, dtype=int)


def calculateBinary(elem):
    # calcola il valore decimale di un numero binario
    value = 0
    indx = 0
    for indx, e in enumerate(elem):
        value = value + e * 2 ** indx
    return value


def calculateSingleCounts(node, data):
    # Dato un nodo della rete bayesiana, viene aggiornato il valore counts con i  nuovi valori dati in Data
    unique, counts = np.unique(data, return_counts=True, axis=1)
    ind = 0
    for i in unique.T:
        for j in range(0, len(i)):
            i[j] = 1 - i[j]
        num = (2 ** (len(node["parents"]) + 1)) - calculateBinary(i) - 1
        node["counts"][num] += counts[ind]
        ind += 1


def calculateCounts(re, bn):
    # Aggiorna i counts di una rete bayesiana con i valori di un dataset
    idxcalc = []
    for i in bn.V:
        idxcalc.append(re[:, bn.node_idx(i)])
        parents = bn.F[i]['parents']
        for p in parents:
            idxcalc.append(re[:, bn.node_idx(p)])
        calculateSingleCounts(bn.F[i], idxcalc)
        idxcalc.clear()


def kullbackLeiblerDivergence(var1, var2):
    # Calcola la divergenza di Kullback-Leiber
    res = 0
    for i in range(0, len(var1)):
        if ((var1[i] / var2[i]) != 0):
            res = var1[i] * log(var1[i] / var2[i], 2)
    return res


def main(pathBN, hyperparameter,
         n, printBN):
    bn = read_bn(pathBN)
    addBNHyperparameter(bn, hyperparameter)
    bn1 = bn.copy()
    numberOfSample = n
    numberOfSample.sort()
    result = []

    re = random_sample(bn, numberOfSample[len(numberOfSample) - 1])
    precNumberOfValue = 0
    for numberOfValue in numberOfSample:
        calculateCounts(re[precNumberOfValue:numberOfValue], bn)
        div = 0
        for i in bn.V:
            calculatePosteriorMarginalization(bn.F[i])
            div = div + kullbackLeiblerDivergence(bn1.F[i]["cpt"], bn.F[i]["cpt"])
        result.append(div)
        precNumberOfValue = numberOfValue
        if (printBN):
            print(bn.F)
    if (printBN):
        print(bn1.F)
    plt.plot(numberOfSample, result)
    plt.ylabel("valori della divergenza")
    plt.xlabel("dimensione dataset")
    plt.show()


pathBN = 'data/asia.bif'  # path della rete bayesiana da caricare
hyperparameter = 1  # hyperparameter impostato su Laplace Smoothing
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 50, 100, 200, 300, 400, 500, 600, 1000, 2000]  # il valore più grande indica la dimensione del dataset
# i valori più piccoli indicano il range di dati del dataset, da far apprendere alla rete, cosi da poterli campionare
printBN = False  # flag per stampare il contenuto dei nodi
main(pathBN, hyperparameter, n, printBN)
