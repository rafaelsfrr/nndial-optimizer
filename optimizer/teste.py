from nn.NNDialogue import NNDial
from optimizer import util
from optimizer import ga

# Entao, o jeito que os caras fizeram foi bem lixo, basicamente eles pegam o arquivo que representa o belief tracker
# treinado e jogam em um arquivo model/CamRest.NDM.model
# depois eh so rodar
#     model = NNDial('adjust', 'config/NDM.cfg')
#     model.trainNet()
# Isso vai treinar o resto da rede. O que vai acontecer eh que as outras redes vao ser escritas no mesmo arquivo
# Depois eh so rodar
# bleu = model.testNet()
# Isso vai carregar de novo a rede e rodar o teste, retornando o bleu

# O fluxo entao vai ser,
# 0) a gente vai inicializar o algoritmo genetico com um vetor inicial de configuracoes
# 1) a gente vai pegar o arquivo model/CamRest.tracker.model e copiar pra model/CamRest.NDM.model
# 2)    model = NNDial('adjust', 'config/NDM.cfg')
# #     model.trainNet()
# 3)    model = NNDial('test', 'config/NDM.cfg')
#       bleu = model.testNet()
# 4)    o bleu vai cair no algoritmo genetico que vai estar em optimizer
# 5)    o algoritmo vai gerar um vetor de configuracoes representando outra geracao
# 6) Essas configuracoes vao ser escritas no arquivo config/NDM.cfg
# 7) Volta ao passo 1


if __name__ == '__main__':

    # load config file
    config = util.load_config_file('config/NDM.cfg', 'learn')

    # get learn config params
    lr, lr_decay, _, _, l2, random_seed, _, _, _, _ = config

    # define chromosomes
    chromosomes = [float(lr), float(lr_decay), float(l2), int(random_seed)]

    # define chromosomes limits
    limits = [[-0.01, 0.01], [0, 1], [0, 0.000001], [1, 8]]

    # get first individuals
    individuals = ga.init(4, chromosomes, limits)

    # save each individual in a config file
    for i in range(0, len(individuals)):
        util.write_config_file(individuals[i], 'config/NDM{}.cfg'.format(i))

    # define the number of generations
    num_generations = 5

    # define the bleu of the experiment
    bleu = []

    # for each generation
    for generation in range(0, num_generations):
        # for each individual, run the net train
        bleu_individual = []
        for individual in range(0, len(individuals)):
            model = NNDial('adjust', 'config/NDM{}.cfg'.format(individual))
            model.trainNet()
            bleu_individual.append(model.testNet())

        # grab the bleu and implement the ga algorithm
        # grab the time of the train
        # plot the graphics

    bleu.append(bleu_individual)
