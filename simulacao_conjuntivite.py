import numpy as np
import matplotlib.pyplot as plt

# Estados
S = 0  # Suscetível
E = 1  # Exposto (incubação)
I = 2  # Infectado (transmite)
R = 3  # Recuperado

# Parâmetros do modelo
grid_size = 50
infection_prob = 0.40      # Probabilidade de contágio ao tocar um vizinho I
min_incub = 2
max_incub = 4
min_infec = 5
max_infec = 7
initial_infected = 6

# Grade e temporizadores
grid = np.zeros((grid_size, grid_size), dtype=int)
incubation = np.zeros((grid_size, grid_size), dtype=int)
infection_timer = np.zeros((grid_size, grid_size), dtype=int)

# Infectados iniciais
for _ in range(initial_infected):
    x, y = np.random.randint(0, grid_size, size=2)
    grid[x, y] = I
    infection_timer[x, y] = np.random.randint(min_infec, max_infec + 1)

# Função de atualização
def update():
    global grid, incubation, infection_timer
    
    new_grid = grid.copy()
    
    for i in range(grid_size):
        for j in range(grid_size):
            
            # SUSCETÍVEL → ver vizinhos
            if grid[i, j] == S:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < grid_size and 0 <= nj < grid_size:
                            if grid[ni, nj] == I and np.random.rand() < infection_prob:
                                new_grid[i, j] = E
                                incubation[i, j] = np.random.randint(min_incub, max_incub + 1)
                                break
            
            # EXPOSTO → pode virar infectado
            elif grid[i, j] == E:
                incubation[i, j] -= 1
                if incubation[i, j] <= 0:
                    new_grid[i, j] = I
                    infection_timer[i, j] = np.random.randint(min_infec, max_infec + 1)
            
            # INFECTADO → pode virar recuperado
            elif grid[i, j] == I:
                infection_timer[i, j] -= 1
                if infection_timer[i, j] <= 0:
                    new_grid[i, j] = R
    
    grid = new_grid.copy()
    return grid

# Captura de snapshots
snapshots = []
frames = [5, 10, 20, 40, 60, 100]

for step in range(max(frames) + 1):
    update()
    if step in frames:
        snapshots.append(grid.copy())

# Plot dos snapshots
fig, axes = plt.subplots(2, 3, figsize=(11, 6))

cmap = plt.cm.get_cmap("viridis", 4)

for ax, snap, frame in zip(axes.ravel(), snapshots, frames):
    ax.imshow(snap, cmap=cmap, vmin=0, vmax=3)
    ax.set_title(f"Geração {frame}")
    ax.axis("off")

plt.suptitle("Simulação SEIR da Conjuntivite com Autômatos Celulares", fontsize=14)
plt.show()
