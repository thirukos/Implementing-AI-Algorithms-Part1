from asyncore import loop
from pickle import TRUE
import numpy as np
from pyMaze import *
from timeit import *

def get_available_actions(m, x, y):
    actions = []
    for direction, Bool in m.maze_map[(x,y)].items():
        if Bool == 1:
            actions.append(direction)
    return actions

def get_reward(state, target_cell):
    for i in state:
        if i == target_cell:
            return 1000
        else: 
            return -1
    #return reward

def compute_path(start_cell, target_cell, policy):
    current_cell = start_cell
    path = [current_cell]
    while current_cell != target_cell:
        a = policy[current_cell]
        x, y = current_cell
        if a == 'N':
            x = x - 1
        elif a == 'E':
            y = y + 1
        elif a == 'S':
            x = x + 1
        elif a == 'W':
            y = y - 1

        current_cell = (x, y)
        path.append(current_cell)
    return path

def policy_evaluation(m, policy, values, target_cell, discount_factor, threshold):
    cells = list(m.maze_map.keys())

    while True:
        delta = 0
        for i in cells:
            if i == target_cell:
                continue

            prev_value = values[i]
            a = policy[i]
            x, y = i
            if a == 'N':
                x = x - 1
            elif a == 'E':
                y = y + 1
            elif a == 'S':
                x = x + 1
            elif a == 'W':
                y = y - 1

            value = get_reward(i, target_cell) + discount_factor * values[(x, y)]
            values[i] = value

            delta = max(delta, np.abs(prev_value - value))

        if delta < threshold:
            break

    return values

def policy_improvement(m, actions, policy, values, target_cell, discount_factor):
    cells = list(m.maze_map.keys())

    policy_stable = True
    for i in cells:
        if i == target_cell:
            continue

        old_action = policy[i]
        best_value = -np.inf
        best_action = None
        for a in actions[i]:
            x, y = i
            if a == 'N':
                x = x - 1
            elif a == 'E':
                y = y + 1
            elif a == 'S':
                x = x + 1
            elif a == 'W':
                y = y - 1

            value = get_reward(i, target_cell) + discount_factor * values[(x, y)]
            if value > best_value:
                best_value = value
                best_action = a

        policy[i] = best_action

        if old_action != best_action:
            policy_stable = False

    return policy, policy_stable

def policy_iteration(m, start_cell=None, target_cell=None, discount_factor=0.9, threshold=1e-3):
    if start_cell is None:
        start_cell = list(m.maze_map.keys())[-1]
    if target_cell is None:
        target_cell = list(m.maze_map.keys())[0]

    cells = list(m.maze_map.keys())

    actions = {}
    for i in cells:
        x, y = i
        actions[i] = get_available_actions(m, x, y)

    # Initialize policy
    policy = {}
    for i in actions.keys():
        policy[i] = np.random.choice(actions[i])

    # Initialize value function
    values = {}
    for i in cells:
        if i == target_cell:
            values[i] = 1000
        elif i in actions.keys():
            values[i] = 0
        else:
            values[i] = np.nan

    iteration = 0 

    while True:
        # Policy evaluation
        values = policy_evaluation(m, policy, values, target_cell, discount_factor, threshold)

        # Policy improvement
        policy, policy_stable = policy_improvement(m, actions, policy, values, target_cell, discount_factor)

        if policy_stable:
            break

        iteration += 1

    # Compute path using final policy
    path = compute_path(start_cell, target_cell, policy)

    return path, iteration


if __name__ == '__main__':
    m = maze()
    m.CreateMaze(loadMaze="maze--2023-03-09--11-37-25.csv") # loop percentage = 80% 
    
    forwardPath, iteration = policy_iteration(m, discount_factor = 0.9, threshold = 1e-3)

    a = agent( m, footprints=True, filled=True, color = COLOR.green)
    m.tracePath({a:forwardPath}, delay=50)

    vitime = timeit(stmt = "policy_iteration(m)", number = 10, globals = globals())
    time = textLabel(m, "Timetaken to solve the 30X30 maze, using MDP value iteration: ", vitime)

    pathLength = textLabel(m, "Length of the path ", len(forwardPath)+1)
    VIiteration = textLabel(m, "Total Iteration ", iteration)


    m.run()