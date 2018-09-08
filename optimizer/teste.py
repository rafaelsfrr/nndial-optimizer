import os

from nn.NNDialogue import NNDial
from utils.commandparser import NNSDSOptParser

# Entao, o jeito que os caras fizeram foi bem lixo, basicamente eles pegam o arquivo que representa o belief tracker
# treinado e jogam em um arquivo model/CamRest.NDM.model
# depois eh so rodar
#     model = NNDial('adjust', 'config/NDM.cfg')
#     model.trainNet()
# Isso vai treinar o resto da rede. O que vai acontecer eh que as outras redes vao ser escritas no mesmo arquivo
# Depois eh so rodar
# model = NNDial('test', 'config/NDM.cfg')
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
    model = NNDial('adjust', 'config/NDM.cfg')
    model.trainNet()

    model = NNDial('test', 'config/NDM.cfg')
    bleu = model.testNet()
    os.remove('model/CamRest.NDM.model')
