from itertools import product

import numpy as np

import node

def costruct_bn(path, hyper):
    bayes_n = bayesian_network()

    with open(path, "r") as openfile:
        for line in openfile:
            father = ""
            if not line.find("variable") == -1:
                name = line[line.find(""):line.find("{") - 1].split(" ")[1].strip()
                bayes_n.node[name] = node.node(name, father, "", "")
                bayes_n.name.append(name)
            if not line.find("probability") == -1:
                end_name = min(line.find("|"), line.find(")"))
                if end_name == -1:
                    end_name = line.find(")")
                else:
                    father = line[end_name + 2:line.find(")") - 1]
                    father = father.split(", ")
                name = line[line.find("(") + 2:end_name - 1]
                (bayes_n.node[name]).father = father
                bayes_n.node[name].counts = np.full(2 ** (len(father) + 1), hyper, dtype=int)
            if not line.find("table") == -1:
                dict = []
                dict.append(line[line.find("table") + 5:line.find(",")])
                dict.append(line[line.find(",") + 1:line.find(";")])

                bayes_n.node[name].cpt = list(map(float, dict))

            if ((not line.find("(") == -1) and (not line.find("yes") == -1) or (not line.find("no"))):
                n = 2 ** len(bayes_n.node[name].father)
                dict = []
                for i in range(0, n):
                    value = line[line.find(")") + 1:line.find(";")].split(",")
                    for v in value:
                        dict.append(v)
                    line = openfile.readline()
                bayes_n.node[name].cpt = list(map(float, dict))
    return bayes_n


class bayesian_network:

    def __init__(self):
        self.node = {}
        self.name = []

    def print_network(self):
        print("rete Bayesiana")
        for n in self.node:
            self.node[n].print()

    def calculate_probability_distribution(self):
        result = []
        index = []
        probability = 1
        combination = list(product("01", repeat=len(self.node)))
        for comb in combination:
            for i in self.node:
                index.append(comb[self.name.index(i)])
                parents = self.node[i].father
                for p in parents:
                    index.append(comb[self.name.index(p)])
                prob = self.node[i].get_value_of_cpt(index)
                probability = probability * prob
                index.clear()
            result.append(probability)
            probability = 1
        return [combination, result]

    def train(self, training_set):
        ind_calc = []
        for i in self.node:
            ind_calc.append(training_set[:, self.name.index(i)])
            parents = self.node[i].father
            for p in parents:
                ind_calc.append(training_set[:, self.name.index(p)])
            self.node[i].update_counts(ind_calc)
            self.node[i].update_cpt()
            ind_calc.clear()
