# nndial-opitimizer

The source code of an optimizer developed with a adapted Evolutionary Algorithm for the NNDIAL chatbot. The NNDIAL chatbot can be found at https://github.com/shawnwun/NNDIAL. This code is also under Apache License 2.0.

## Code Structure and Modifications on the NNDIAL code
The optimizer consist of a module that can be found at `optimizer` and a wrapper `optimizer.py`. There is also another module, `notebooks` that make some analysis of the results. The original code of the NNDIAL chatbot had not suffered much modifications, there was just an externalization of the bleu score on the NNDialogue class.

## Quick Start
To run the code you need the same requirements of the NNDIAL chatbot. You can install them with 

```conda install --file requirements.txt```

or with

```pip install -r requirements.txt```

After this, you can run the wrapper

```python optimizer.py```

This will start the dynamics of training and optimization of the chatbot. All the results will be displayed on the console. By default, the genetic algorithm will have this shape:

```
chromossomes: lr, lr_decay, l2, random_seed
number of individuals: 8
number of generations: 15
```
All this configurations need to be set on the optimizer.py file.

## The Evolutionary Algorithm
The Evolutionary Algorithm was implemented in Python 2.7, following three evolutionary operators: selection, crossover and mutation. 

The selection is done based on the BLEU score. For 8 individuals, the 4 individuals with the most score are always selected.

The crossover is implemented with a single point strategy - given two parents selected by a fitness function, we do

```
child1 = concat(parent1[0:middle], parent2[middle:end])
child2 = concat(parent2[0:middle], parent1[middle:end])
```

The mutation of each individual is done on every generation, with the chromossome to be mutated selected on random.

After this, the new generation was build with the parents and the children.

## Results

The results show us a optimization considering the BLEU score. Adopting the values `lr = 0.0087`, `lr_decay = 0.57`, `l2 = 0.0002` and `random_seed = 6`, we find a BLEU score of 0.261. More details about the results can be found on the `notebooks` module.
