from pickle import TRUE
import numpy as np
from pyMaze import maze, agent, COLOR, textLabel
from timeit import *

def get_available_actions(m, x, y):
    actions = []
    for direction, Bool in m.maze_map[(x,y)].items():
        if Bool == 1:
            actions.append(direction)
    return actions

def value_iteration(m, start_cell = None, target_cell = None, discount_factor = 0.9, threshold = 1e-3):
    if start_cell is None:
        start_cell = list(m.maze_map.keys())[-1]
    if target_cell is None:
        target_cell = list(m.maze_map.keys())[0]

    cells = list(m.maze_map.keys())

    rewards = {}
    for i in cells:
        if i == target_cell:
            rewards[i] = 1000
        else:
            rewards[i] = -1

    actions = {}
    for i in cells:
        x, y = i
        actions[i] = get_available_actions(m, x, y)

    policy = {}
    for i in actions.keys():
        policy[i] = np.random.choice(actions[i])

    values = {}
    for i in cells:
        if i == target_cell:
            values[i] = 1000
        if i in actions.keys():
            values[i] = -1

    iteration = 0 

    while True:
        diff = 0
        for i in cells:
            prev_value = values[i]
            curr_value = 0

            for a in actions[i]:
                if a == 'N':
                    x = [i[0]-1, i[1]]
                if a == 'E':
                    x = [i[0], i[1]+1]
                if a == 'W':
                    x = [i[0], i[1]-1]
                if a == 'S':
                    x = [i[0]+1, i[1]]
                 
                value = rewards[i] + (discount_factor * values[tuple(x)])
                if value > curr_value:
                    curr_value = value
                    policy[i] = a

            values[i] = curr_value
            diff = max(diff, np.abs(prev_value - values[i]))
            #print(diff)

        if diff < threshold:
            break

        iteration += 1

    value_iter_path = []
    currentCell = start_cell

    value_iter_path.append(currentCell)
    while True:
        direction = policy[currentCell]
        if direction == 'N':
            currentCell = (currentCell[0]-1, currentCell[1])
        if direction == 'E':
            currentCell = (currentCell[0], currentCell[1]+1)
        if direction == 'W':
            currentCell = (currentCell[0], currentCell[1]-1)
        if direction == 'S':
            currentCell = (currentCell[0]+1, currentCell[1])

        value_iter_path.append(currentCell)
        print(currentCell)

        if currentCell == target_cell:
            break

    return value_iter_path, iteration

if __name__ == '__main__':
    m = maze()
    m.CreateMaze(loadMaze="maze--2023-03-12--09-33-14.csv") # loop percentage = 80% 
    
    forwardPath, iteration = value_iteration(m, discount_factor = 0.9, threshold = 1e-3)

    a = agent( m, footprints=True, filled=True, color = COLOR.green)
    m.tracePath({a:forwardPath}, delay=50)

    #vitime = timeit(stmt = "value_iteration(m)", number = 10, globals = globals())
    #time = textLabel(m, "Timetaken to solve the 30X30 maze, using MDP value iteration: ", vitime)

    pathLength = textLabel(m, "Length of the path ", len(forwardPath)+1)
    VIiteration = textLabel(m, "Total Iteration ", iteration)


    m.run()