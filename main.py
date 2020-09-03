from matplotlib.pyplot import ylabel, plot, show, xlabel

import bayesian_network as bn
import tool


def main(path_bn="data/asia.bif",
         hyperparameter=1,
         size_of_training_sets=None, print_bn=False):
    if size_of_training_sets is None:
        size_of_training_sets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 50, 100, 200, 300, 400, 500, 600, 1000, 2000,3000,4000,5000]

    bayes = bn.costruct_bn(path_bn, hyperparameter)
    size_of_training_sets.sort()
    result = []
    training_set = tool.generate_dataset(bayes.calculate_probability_distribution(),
                                         size_of_training_sets[len(size_of_training_sets) - 1])

    prec_training_value = 0
    distribuction_p = bayes.calculate_probability_distribution()

    for current_training_quantity in size_of_training_sets:
        bayes.train(training_set[prec_training_value:current_training_quantity])
        distribuction_qn = bayes.calculate_probability_distribution()

        result.append(tool.kullback_leibler_divergence(distribuction_p, distribuction_qn))
        prec_training_value = current_training_quantity
        if print_bn:
            print(bayes.name)
    if print_bn:
        print(bayes.print_network())
    plot(size_of_training_sets, result)
    ylabel("divergenza")
    xlabel("dimensione dataset")
    show()
    print(size_of_training_sets)
    print(result)


main()
