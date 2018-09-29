import numpy
import copy


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


def select_mating_pool(pop, fitness, num_parents):
    """
    :param pop: the population list
    :param fitness: the fitness list
    :param num_parents: the number of parents
    :return: the parents
    """
    parents = numpy.empty((num_parents, len(pop[0])), dtype=numpy.float)
    bleu = fitness[:]
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(bleu == numpy.max(bleu))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num][:] = pop[max_fitness_idx][:]
        bleu[max_fitness_idx] = -9999999999
    return parents


def crossover(parents, offspring_size):
    """
    :param parents: the individuals
    :param offspring_size: the size of the new generation
    :return: the new generation
    """

    offspring = copy.copy(parents)
    crossover_point = numpy.uint8(offspring_size / 2) + 1
    first_half = copy.copy(offspring[1][0:crossover_point])
    second_half = copy.copy(offspring[0][0:crossover_point])
    offspring[0][0:crossover_point] = first_half
    offspring[1][0:crossover_point] = second_half

    return offspring


def mutation(offspring_crossover):
    """
    :param offspring_crossover: the population
    :return: the new population with a gene of each individual mutated
    """

    # define chromosomes limits
    limits = [[-0.0008, 0.0008], [-0.05, 0.05], [0, 0.0001], [1, 5]]
    # Mutation changes a single gene in each offspring randomly.
    offspring_crossover_copy = copy.copy(offspring_crossover)
    for idx in range(len(offspring_crossover_copy)):
        # the gene to be mutated
        gene = numpy.random.random_integers(0, len(offspring_crossover_copy[idx]) - 1)
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(limits[gene][0], limits[gene][1])
        offspring_crossover_copy[idx][gene] = abs(offspring_crossover_copy[idx][gene] + random_value)
    return offspring_crossover_copy
