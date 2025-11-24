import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# -----------------------------------
# DEFINIÇÃO DOS ESTADOS
# -----------------------------------
S = 0  # Suscetível
E = 1  # Exposto (infectado incubando)
I = 2  # Infectante (transmite conjuntivite)
R = 3  # Recuperado

# -----------------------------------
# PARÂMETROS DO MODELO
# -----------------------------------
grid_size = 40                  # tamanho da matriz
initial_infected = 5            # infectados iniciais
infection_prob = 0.40           # probabilidade de contágio ao ter vizinho infectado
min_incub = 2                   # incubação mínima (dias)
max_incub = 4                   # incubação máxima (dias)
infection_time = 5              # tempo de infecção ativa
iterations = 110                # número de gerações

# -----------------------------------
# GRADE E CONTADORES
# -----------------------------------
grid = np.zeros((grid_size, grid_size), dtype=int)
incub_timer = np.zeros((grid_size, grid_size), dtype=int)
infect_timer = np.zeros((grid_size, grid_size), dtype=int)

# adiciona infectados iniciais
for _ in range(initial_infected):
    x, y = np.random.randint(0, grid_size, size=2)
    grid[x, y] = I
    infect_timer[x, y] = infection_time

# -----------------------------------
# FUNÇÃO PARA PEGAR VIZINHOS (VIZINHANÇA DE MOORE)
# -----------------------------------
def get_neighbors(i, j):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            ni, nj = i + dx, j + dy
            if 0 <= ni < grid_size and 0 <= nj < grid_size:
                neighbors.append((ni, nj))
    return neighbors

# -----------------------------------
# A TUALIZAÇÃO DO AUTÔMATO CELULAR
# -----------------------------------
def update():
    global grid, incub_timer, infect_timer

    new_grid = grid.copy()

    for i in range(grid_size):
        for j in range(grid_size):

            # estado SUSCETÍVEL → pode ser exposto por vizinhos infectados
            if grid[i, j] == S:
                neighbors = get_neighbors(i, j)
                for ni, nj in neighbors:
                    if grid[ni, nj] == I:
                        if random.random() < infection_prob:
                            new_grid[i, j] = E
                            incub_timer[i, j] = random.randint(min_incub, max_incub)
                            break

            # estado EXPOSTO → incubando
            elif grid[i, j] == E:
                incub_timer[i, j] -= 1
                if incub_timer[i, j] <= 0:
                    new_grid[i, j] = I
                    infect_timer[i, j] = infection_time

            # estado INFECTADO → transmite e depois recupera
            elif grid[i, j] == I:
                infect_timer[i, j] -= 1
                if infect_timer[i, j] <= 0:
                    new_grid[i, j] = R

            # estado RECUPERADO → não faz nada
            # (poderia ter perda de imunidade se quiser)

    grid = new_grid.copy()

# -----------------------------------
# SIMULAÇÃO E CAPTURA DE FRAMES
# -----------------------------------
snapshots = []
frames_to_save = [1, 5, 10, 20, 40, 60, 80, 100]

for t in range(iterations):
    update()
    if t in frames_to_save:
        snapshots.append(grid.copy())

# -----------------------------------
# PLOTAGEM DOS RESULTADOS
# -----------------------------------
fig, axes = plt.subplots(2, 4, figsize=(12, 6))

titles = [f"Geração {f}" for f in frames_to_save]

for ax, snap, title in zip(axes.ravel(), snapshots, titles):
    sns.heatmap(
        snap,
        ax=ax,
        cmap="viridis",
        cbar=False,
        square=True,
        linewidths=0.1,
        linecolor="black"
    )
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
