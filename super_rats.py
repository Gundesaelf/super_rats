# |---------------------------------INSTRUCTIONS---------------------------------|

'''
Giant Rat Genetic Algorithm Simulation

This program simulates the evolution of a population of rats toward a 
target average weight using a simple genetic algorithm.

Features:
- Initializes a population of rats with random weights.
- Selects a specified number of males and females each generation to breed.
- Breeding produces offspring with weights influenced by parents.
- Offspring may mutate according to user-specified probability and magnitude.
- Tracks average population weight and fitness toward a goal.
- Stops when the population reaches the target weight or a generation limit.

User-configurable parameters:
- NUM_MALES: Number of males retained for breeding.
- MUTATE_ODDS: Probability that an offspring mutates.
- MUTATE_MIN / MUTATE_MAX: Minimum and maximum mutation multipliers.

Usage:
- Modify user parameters at the top of the file.
- Run the script to see generation-by-generation fitness and average weights.
'''

# |---------------------------------IMPORTS---------------------------------|

import random
import time
import statistics

# |---------------------------------USER_INPUTS---------------------------------|

# qty of male rats to start with
NUM_MALES = 4

# chance of mutation occurring
MUTATE_ODDS = 0.01

# how drastic a mutation is
MUTATE_MIN = 0.5 # size % that a rat will shrink relative to current size; default 50%
MUTATE_MAX = 1.2 # size % that a rat will grow relative to current size; default 120%

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE

# |---------------------------------CONSTANTS---------------------------------|

# WEIGHTS ARE IN GRAMS
GOAL = 50000
NUM_RATS = 20
NUM_FEMALES = NUM_RATS - NUM_MALES
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# ensure an even number of rats for breeding pairs
if NUM_RATS & 1:
    NUM_RATS += 1

# |---------------------------------FUNCTIONS---------------------------------|

def populate(num_rats, min_wt, max_wt, mode_wt):
    ''' Initialize a population with a triangular distribution of weights '''
    return [int(random.triangular(min_wt, max_wt, mode_wt)) for i in range(num_rats)]

def fitness(population, goal):
    ''' Measure population fitness based on an attribute mean vs target '''
    avg = statistics.mean(population)
    return avg / goal

def select(population, num_males, num_females):
    ''' Cull a population to retain only a specified number of members '''
    sorted_pop = sorted(population)

    members_per_gender = len(sorted_pop) // 2

    females = sorted_pop[:members_per_gender]
    males = sorted_pop[members_per_gender:]

    largest_females = females[-num_females:]
    largest_males = males[-num_males:]

    return largest_males, largest_females

def breed(males, females, litter_size):
    ''' Crossover genes among members (weights) of a population '''
    random.shuffle(males)
    random.shuffle(females)

    children = []

    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(min(female, male), max(female, male))
            children.append(child)

    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    ''' Randomly alter rat weights using input odds & fractional changes '''
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat * random.uniform(mutate_min, mutate_max))

    return children

def main():
    ''' Initialize population, select, breed, & mutate, display results '''
    generations = 0

    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    print(f'Initial pop weights: {parents}')
    
    pop_fitness = fitness(parents, GOAL)
    print(f'Initial pop fitness: {pop_fitness}')
    print(f'Number to retain: {NUM_RATS}')

    avg_wt = []

    while pop_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents, NUM_MALES, NUM_FEMALES)

        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)

        parents = selected_males +  selected_females + children

        pop_fitness = fitness(parents, GOAL)
        print(f'Generation {int(generations)} fitness = {pop_fitness}')

        avg_wt.append(int(statistics.mean(parents)))

        generations += 1

    print(f'AVG WT per generation: {avg_wt}')
    print(f'\nNum of generations: {generations}')
    print(f'Number of years: {int(generations/LITTERS_PER_YEAR)}')

# |---------------------------------MAIN_LOOP---------------------------------|

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()
    total = end - start

    print(f'Runtime: {total}s')
