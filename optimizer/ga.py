import numpy


def init(num_individuals, chromosomes, limits):
    """
    :param num_individuals: the number of individuals
    :param chromosomes: a list with the initial chromosomes values
    :param limits: a matrix representing the limits of the chromosomes values
    :return: a matrix representing the individuals
    """

    individuals = []
    for i in range(0, num_individuals):
        individual = []
        for j in range(0, len(chromosomes)):
            individual.append(chromosomes[j] + numpy.random.uniform(limits[j][0], limits[j][1]))
        individuals.append(individual)
    return individuals


if __name__ == '__main__':
    chromosomes = [0.008, 0.5, 0.0001, 1]
    limits = [[-0.01, 0.01], [0, 1], [0, 0.000001], [1, 8]]

    print init(2, chromosomes, limits)
