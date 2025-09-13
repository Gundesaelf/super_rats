## Super Rats

A Giant Rat Genetic Algorithm Simulation

This Python program simulates the evolution of a population of rats toward a target average weight using a simple genetic algorithm. It is inspired by the exercises in *Impractical Python Projects*.

## Features

- Initializes a population of rats with random weights.
- Selects a specified number of males and females each generation to breed.
- Breeding produces offspring with weights influenced by parents.
- Offspring may mutate according to user-specified probability and magnitude.
- Tracks average population weight and fitness toward a goal.
- Stops when the population reaches the target weight or after a set number of generations.

## User-Configurable Parameters

These are located at the top of the script:

| Parameter    | Description |
| ------------ | ----------- |
| `NUM_MALES`  | Number of males retained for breeding each generation. |
| `MUTATE_ODDS` | Probability that an offspring mutates (0–1). |
| `MUTATE_MIN` | Minimum mutation multiplier (fractional shrink, e.g., 0.5). |
| `MUTATE_MAX` | Maximum mutation multiplier (fractional growth, e.g., 1.2). |

## How to Run

1. Clone this repository or download the script.
2. Open the script and adjust the user parameters if desired.
3. Run the script with Python 3:

```bash
python super_rats.py

```
🔗 Connect with me https://www.linkedin.com/in/chris-gundes
