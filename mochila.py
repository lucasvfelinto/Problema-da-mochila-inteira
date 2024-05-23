import random
# Function to calculate the fitness of an individual

# Function to calculate the fitness of an individual
def fitness(individual, weights, values, W):
    total_weight = sum(ind * w for ind, w in zip(individual, weights))
    total_value = sum(ind * v for ind, v in zip(individual, values))
    if total_weight > W:
        return 0  # Penalize overweighted individuals
    return total_value

# Function to generate a random individual
def generate_individual(n):
    return [random.randint(0, 1) for _ in range(n)]

# Function to generate a population of individuals
def create_population(size, n):
    return [generate_individual(n) for _ in range(size)]

# Function to select the best individuals
def tournament_selection(population, weights, values, W, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda ind: fitness(ind, weights, values, W), reverse=True)
    return selected[0]

# Function to perform a crossover of a point
def one_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Function to perform a mutation
def mutate(individual, mutation_rate):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]

# Function to perform a genetic algorithm 
def genetic_algorithm(weights, values, W, population_size=200, generations=1000, mutation_rate=0.01):
    n = len(weights)
    population = create_population(population_size, n)
    
    best_solution = None
    best_fitness = 0

    for generation in range(generations):
        new_population = []
        
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, weights, values, W)
            parent2 = tournament_selection(population, weights, values, W)
            offspring1, offspring2 = one_point_crossover(parent1, parent2)
            new_population.extend([mutate(offspring1, mutation_rate), mutate(offspring2, mutation_rate)])
        
        population = new_population
        
        # Find the best individual in the population
        current_best_individual = max(population, key=lambda ind: fitness(ind, weights, values, W))
        current_best_fitness = fitness(current_best_individual, weights, values, W)
        if current_best_fitness > best_fitness:
            best_solution = current_best_individual
            best_fitness = current_best_fitness
    
    return best_solution, best_fitness

# Example of use
n = 3
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

best_solution, best_value = genetic_algorithm(weights, values, W)
print("Melhor Solução: ", best_solution)
print("Valor Total: ", best_value)