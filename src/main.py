from genetic_algorithm import genetic_algorithm, start, end, obstacles, GRID_SIZE
from visualization import plot_path

if __name__ == '__main__':
    best_path = genetic_algorithm()
    plot_path(best_path, obstacles, start, end, GRID_SIZE)
    
