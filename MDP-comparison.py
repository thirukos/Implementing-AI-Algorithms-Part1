from MDP_PolicyIteration import *
from MDP_ValueIteration import *
from pyMaze import *
from timeit import timeit
from memory_profiler import memory_usage

def run_policy_iteration(myMaze):
    return policy_iteration(myMaze, discount_factor=0.4, threshold=1e-3)

def run_value_iteration(myMaze):
    return value_iteration(myMaze, discount_factor=0.9, threshold=1e-3)

if __name__ == '__main__':
    myMaze = maze()
    myMaze.CreateMaze(loadMaze="maze--2023-03-12--09-33-14.csv") # loop percentage = 80% 

    policyI_forwardPath, policyI_iteration = run_policy_iteration(myMaze)
    policyI_memory_usage = memory_usage((run_policy_iteration, (myMaze,), {}))
    
    valueI_forwardPath, valueI_iteration = run_value_iteration(myMaze)
    valueI_memory_usage = memory_usage((run_value_iteration, (myMaze,), {}))
    
    agent_policyI = agent(myMaze, footprints=True, shape='square', filled=True,color = COLOR.green)
    agent_valueI = agent(myMaze, footprints=True, shape='square', color = COLOR.blue)

    myMaze.tracePath({agent_policyI:policyI_forwardPath}, delay=100)
    myMaze.tracePath({agent_valueI:valueI_forwardPath}, delay=100)

    #path length
    policyI_pathLength = textLabel(myMaze, "MDP-PI PathLength ", len(policyI_forwardPath))
    valueI_pathLength = textLabel(myMaze, "MDP-VI PathLength ", len(valueI_forwardPath))

    #iteration
    policyI_Iteratio = textLabel(myMaze, "MDP-PI Iteration ", policyI_iteration)
    valueI_Iteratio = textLabel(myMaze, "MDP-VI Iteration ", valueI_iteration)

    #time
    policyI_time = textLabel(myMaze, "MDP-PI time: ", timeit(stmt = "run_policy_iteration(myMaze)", number = 10, globals = globals()))
    valueI_time = textLabel(myMaze, "MDP-VI time: ", timeit(stmt = "run_value_iteration(myMaze)", number = 10, globals = globals()))

    #memory usage
    policyI_memory = textLabel(myMaze, "MDP-PI memory: ", f"{max(policyI_memory_usage):.2f} MB")
    valueI_memory = textLabel(myMaze, "MDP-VI memory: ", f"{max(valueI_memory_usage):.2f} MB")

    myMaze.run()
