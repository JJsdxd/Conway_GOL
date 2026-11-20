import rules
import numpy as np
import matplotlib.pyplot as plt
import time
simulation_steps = int(input("Enter number of steps to be simulated :"))*10
sizer = int(input("Enter side length"))

grid = np.random.choice([0,1],size = (sizer,sizer))
row,cols = grid.shape
next_grid = np.zeros((row,cols),dtype=int)
plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap="binary", vmin=0, vmax=1)
ax.axis("off")

target_fps = 15
delta_time = 1.0/target_fps


i = 0
while i < simulation_steps:
    print(f"Sim_step {i}")
    frame_start_time = time.perf_counter()
    for j in range(cols):
        for k in range(row):
            cell_status = grid[k,j]
            alive_neighbour_count = 0
            if k!=0:
                if grid[k-1][j]:
                    alive_neighbour_count = alive_neighbour_count + 1
                if j != cols - 1 and k != row - 1:
                    if grid[k-1][j+1]:
                        alive_neighbour_count = alive_neighbour_count + 1
                    if grid[k+1][j]:
                        alive_neighbour_count = alive_neighbour_count + 1
            if j!=0:
                if j != cols - 1 and k != row - 1:
                    if grid[k][j+1]:
                        alive_neighbour_count = alive_neighbour_count + 1
                    if grid[k+1][j+1]:
                        alive_neighbour_count = alive_neighbour_count + 1
                    if grid[k][j-1]:
                        alive_neighbour_count = alive_neighbour_count + 1
                    if grid[k+1][j-1]:
                        alive_neighbour_count = alive_neighbour_count + 1
                    if grid[k-1][j-1]:
                        alive_neighbour_count = alive_neighbour_count + 1
            next_grid[k][j] =  int(rules.cell_next_state_isAlive(cell_status,alive_neighbour_count))
    elapsed = time.perf_counter() - frame_start_time
    sleep_time = max(0.001, delta_time - elapsed)
    if (sleep_time == 0.001):
        print(f" too low sleep_time {sleep_time}")
    plt.pause(sleep_time)
    grid = next_grid
    img.set_data(grid)
    i= i + 1
print(f"Simulation complete")
plt.ioff()
plt.show()