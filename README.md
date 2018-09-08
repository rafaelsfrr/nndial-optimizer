# nndial-optmizer

## Recomendações iniciais
Instalem o anaconda ou o miniconda e criem um ambiente virtual. Lembrem-se que o python utilizado pelo chatbot é a versão 2.7.

## Dependências
Todas as dependências estão declaradas no arquivo requirements.txt

Para instalá-las, basta executar:

`conda install --file requirements.txt`

## Variáveis de ambiente
Defina a variável de ambiente

`THEANO_FLAGS = optimizer=fast_compile,device=cuda*,floatX=float32`

## Estrutura do diretório
`optimizer` -> Módulo do algoritmo genético

`notebooks` -> Módulo principal onde vamos chamar toda a estrutura de treinamento e execução da rede
Todos os outros módulos e arquivos são referentes ao NNDIAL.
