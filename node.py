import numpy as np

import tool


class node:

    def __init__(self, name, father, cpt, hyper):
        self.father = father
        self.cpt = cpt
        self.name = name
        self.counts = hyper

    def print(self):
        print("________________")
        print("name " + self.name)
        print("cpt:")
        print(self.cpt)
        print("father:")
        print(self.father)
        print("hyper:")
        print(self.counts)
        print("________________")

    def get_value_of_cpt(self, index_of_element):
        index_of_element = list(map(int, index_of_element))
        num = (2 ** (len(self.father) + 1)) - tool.calculate_binary_value(index_of_element) - 1
        return self.cpt[num]

    def update_cpt(self):
        total = []
        len_par = int(2 ** len(self.father))
        num = int(len(self.counts) / len_par)
        for i in range(0, len_par):
            total.append(sum(self.counts[0 + num * i:num + num * i]))
        j = 0
        for i in self.counts:
            self.cpt[j] = round(i / total[int(j / num)], 2)
            j += 1

    def update_counts(self, data):
        unique, counts = np.unique(data, return_counts=True, axis=1)
        ind = 0
        for i in unique.T:
            # for j in range(0, len(i)):
            #    i[j] = 1 - i[j]
            num = (2 ** (len(self.father) + 1)) - tool.calculate_binary_value(i) - 1
            self.counts[num] = self.counts[num] + counts[ind]
            ind = ind + 1
