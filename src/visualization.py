import matplotlib.pyplot as plt

def plot_path(path, obstacles, start, end, grid_size=(100, 100)):
    fig, ax = plt.subplots()
    x, y = zip(*path)
    
    if obstacles:
        ox, oy = zip(*obstacles)
        ax.scatter(ox, oy, color='r', label='Obstacles')
    
    ax.plot(x, y, marker='o', color='b', label='Path')
    ax.scatter(*start, color='g', s=100, label='Start')
    ax.scatter(*end, color='g', s=100, label='End')
    
    ax.set_xlim(0, grid_size[0])
    ax.set_ylim(0, grid_size[1])
    ax.set_title('Optimal Flight Path with Obstacles')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.show()
