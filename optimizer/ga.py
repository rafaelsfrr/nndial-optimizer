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


def select_mating_pool(pop, fitness, num_parents):
    """
    :param pop: the population list
    :param fitness: the fitness list
    :param num_parents: the number of parents
    :return: the parents
    """
    parents = numpy.empty((num_parents, len(pop[0])))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num][:] = pop[max_fitness_idx][:]
        fitness[max_fitness_idx] = -9999999999
    return parents


def crossover(parents, offspring_size):
    """
    :param parents: the individuals
    :param offspring_size: the size of the new generation
    :return: the new generation
    """
    offspring = [[]]
    # The point at which crossover takes place between two parents. Usually it is at the center.
    crossover_point = numpy.uint8(offspring_size / 2)
    for k in range(offspring_size):
        # Index of the first parent to mate.
        parent1_idx = k % len(parents[0])
        # Index of the second parent to mate.
        parent2_idx = (k + 1) % len(parents[0])

        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k][0:crossover_point] = parents[parent1_idx][0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k][crossover_point:] = parents[parent2_idx][crossover_point:]
    return offspring


def mutation(offspring_crossover):
    """
    :param offspring_crossover: the population
    :return: the new population with a gene of each individual mutated
    """
    # define chromosomes limits
    limits = [[-0.0008, 0.0008], [-0.05, 0.05], [0, 0.0001], [1, 5]]
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(len(offspring_crossover)):
        # the gene to be mutated
        gene = numpy.random.random_integers(0, len(offspring_crossover[idx]) - 1)
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(limits[gene][0], limits[gene][1])
        offspring_crossover[idx][gene] = offspring_crossover[idx][gene] + random_value
    return offspring_crossover


if __name__ == '__main__':
    bleu = [1, 2, 3, 4]
    individuals = [[0.1, 0.3, 0.2, 0.4], [0.1, 0.1, 0.19, 0.9], [0.1, 0.1, 0.2, 0.1], [0.1, 0.2, 0.2, 0.2]]

    parents = select_mating_pool(individuals, bleu, 2)

    nindividuals = crossover(parents, 1)

    nindividuals_mutated = mutation(nindividuals)

    print 'bleu: {}'.format(bleu)
    print 'individuals: {}'.format(individuals)
    print 'parents: {}'.format(parents)
    print 'nindividuals: {}'.format(nindividuals)
    print 'nindividuals_mutated: {}'.format(nindividuals_mutated)
