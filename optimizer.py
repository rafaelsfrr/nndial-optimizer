from nn.NNDialogue import NNDial
from optimizer import util
from optimizer import ga
import time


if __name__ == '__main__':

    # load config file
    config = util.load_config_file('config/NDM.cfg', 'learn')

    # get learn config params
    lr, lr_decay, _, _, l2, random_seed, _, _, _, _ = config

    # define the number of generations
    num_generations = 30

    # define the number of individuals
    num_individuals = 8

    # define chromosomes
    chromosomes = [float(lr), float(lr_decay), float(l2), int(random_seed)]

    # define chromosomes limits
    limits = [[-0.0008, 0.0008], [-0.05, 0.05], [0, 0.0001], [1, 5]]

    # get first individuals
    individuals = ga.init(num_individuals, chromosomes, limits)

    # save each individual in a config file
    for i in range(0, len(individuals)):
        util.write_config_file(individuals[i], 'config/NDM{}.cfg'.format(i))

    # define the bleu of the experiment
    bleu = []
    time_vec = []

    # for each generation
    for generation in range(0, num_generations):
        # for each individual, run the net train
        bleu_generation = []
        time_generation = []
        print 'Starting the generation {} with the individuals {}'.format(generation, individuals)
        for individual in range(0, len(individuals)):
            util.move_file('model/CamRest.tracker.model', 'model/CamRest.NDM.model')
            args = util.make_args('config/NDM{}.cfg'.format(individual), 'adjust')
            config = args.config
            time_init = time.time()
            model = NNDial(config, args)
            print 'Starting the training of the individual {} of the generation number {}'.format(individual, generation)
            model.trainNet()
            time_end = time.time()
            time_total = (time_end - time_init) / 60.0
            time_generation.append(time_total)
            args = util.make_args('config/NDM{}.cfg'.format(individual), 'test')
            config = args.config
            model = NNDial(config, args)
            bleu_generation.append(model.testNet())
            util.remove_file('model/CamRest.NDM.model')

        bleu.append(bleu_generation[:])
        parents = ga.select_mating_pool(individuals, bleu_generation, 4)
        print 'Selected parents for the next generation {}'.format(parents)
        nindividuals_1 = ga.crossover(parents[0:2], 2)
        nindividuals_2 = ga.crossover(parents[2:4], 2)
        nindividuals = list()
        nindividuals.append(parents[0][:].tolist())
        nindividuals.append(parents[1].tolist())
        nindividuals.append(parents[2][:].tolist())
        nindividuals.append(parents[3][:].tolist())
        nindividuals.append(nindividuals_1[0][:].tolist())
        nindividuals.append(nindividuals_1[1][:].tolist())
        nindividuals.append(nindividuals_2[0][:].tolist())
        nindividuals.append(nindividuals_2[1][:].tolist())
        individuals = ga.mutation(nindividuals)
        print 'Selected individuals for the next generation {}'.format(individuals)
        time_vec.append(time_generation)
        print 'time after {} generations: {} min'.format(num_generations, time_vec)
        print 'bleu after {} generations: {}'.format(num_generations, bleu)

    print 'time final: {} min'.format(time_vec)
    print 'bleu final: {}'.format(bleu)
