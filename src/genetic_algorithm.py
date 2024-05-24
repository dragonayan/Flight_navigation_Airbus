import numpy as np
import random
import math
import json

POPULATION_SIZE = 50
MUTATION_RATE = 0.01
NUM_GENERATIONS = 1000
GRID_SIZE = (100, 100)

start = (0, 0)
end = (99, 99)

def load_obstacles(filename='./data/sample_data.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    weather_conditions = data['weather'][0]['main']
    obstacles = []
    if weather_conditions in ['Rain', 'Snow', 'Fog','Clouds']:
        obstacles = [(i, i) for i in range(10, 20)]
    return obstacles

obstacles = load_obstacles()

def create_chromosome():
    path = [start]
    while path[-1] != end:
        x, y = path[-1]
        next_steps = [(x + dx, y + dy) for dx, dy in [(1, 0), (0, 1)] if 0 <= x + dx < GRID_SIZE[0] and 0 <= y + dy < GRID_SIZE[1]]
        next_step = random.choice(next_steps)
        path.append(next_step)
    return path

def initialize_population():
    return [create_chromosome() for _ in range(POPULATION_SIZE)]

def fitness(chromosome):
    if chromosome[-1] != end:
        return float('inf')
    total_distance = sum(math.dist(chromosome[i], chromosome[i+1]) for i in range(len(chromosome)-1))
    obstacle_penalty = sum(1 for point in chromosome if point in obstacles)
    return total_distance + (obstacle_penalty * 1000)

def selection(population):
    population = sorted(population, key=lambda x: fitness(x))
    return population[:POPULATION_SIZE//2]

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1)-1)
    child = parent1[:cut] + parent2[cut:]
    if child[-1] != end:
        child = adjust_path_to_end(child)
    return child

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        index = random.randint(1, len(chromosome)-2)
        chromosome[index] = (chromosome[index][0] + random.choice([0, 1]), chromosome[index][1] + random.choice([0, 1]))
    if chromosome[-1] != end:
        chromosome = adjust_path_to_end(chromosome)
    return chromosome

def adjust_path_to_end(path):
    while path[-1] != end:
        x, y = path[-1]
        if x < end[0]:
            x += 1
        if y < end[1]:
            y += 1
        path.append((x, y))
    return path

def genetic_algorithm():
    population = initialize_population()
    for generation in range(NUM_GENERATIONS):
        selected_population = selection(population)
        next_population = selected_population[:]
        while len(next_population) < POPULATION_SIZE:
            parent1, parent2 = random.sample(selected_population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_population.append(child)
        population = next_population
    best_path = min(population, key=lambda x: fitness(x))
    return best_path