from MDP_PolicyIteration import *
from MDP_ValueIteration import *
from BreadthFirstSearch import BFS
from DepthFirstSearch import DFS 
from Astar import Astar, ManhattanDist
from pyMaze import *
from timeit import timeit
from memory_profiler import memory_usage


def run_policy_iteration(myMaze):
    return policy_iteration(myMaze, discount_factor=0.9, threshold=1e-3)

def run_value_iteration(myMaze):
    return value_iteration(myMaze, discount_factor=0.9, threshold=1e-3)


if __name__ == '__main__':
    myMaze = maze(30, 30)
    myMaze.CreateMaze(loadMaze="maze--2023-03-09--11-37-25.csv") # loop percentage = 80% 

    bfs_searchSpace, bfs_reversePath, bfs_forwardPath = BFS(myMaze)
    dfs_searchSpace, dfs_reversePath, dfs_forwardPath = DFS(myMaze)
    astar_searchSpace, astar_reversePath, astar_forwardPath = Astar(myMaze)
    policyI_forwardPath, policyI_iteration = run_policy_iteration(myMaze)
    valueI_forwardPath, valueI_iteration = run_value_iteration(myMaze)
    
    agent_BFS = agent(myMaze, footprints=True, shape='square', filled=True,color = COLOR.green)
    agent_DFS = agent(myMaze, footprints=True, shape='square', filled=True, color = COLOR.blue)
    agent_Astar = agent(myMaze, footprints=True, shape='square', color = COLOR.yellow)
    agent_policyI = agent(myMaze, footprints=True, shape='square', filled=True,color = COLOR.red)
    agent_valueI = agent(myMaze, footprints=True, shape='square', color = COLOR.cyan)

    myMaze.tracePath({agent_BFS:bfs_forwardPath}, delay=100)
    myMaze.tracePath({agent_DFS:dfs_forwardPath}, delay=100)
    myMaze.tracePath({agent_Astar:astar_forwardPath}, delay=100)
    myMaze.tracePath({agent_policyI:policyI_forwardPath}, delay=100)
    myMaze.tracePath({agent_valueI:valueI_forwardPath}, delay=100)

    #path length
    bfs_pathLength = textLabel(myMaze, "BFS PathLength ", len(bfs_forwardPath)+1)
    dfs_pathLength = textLabel(myMaze, "DFS PathLength ", len(dfs_forwardPath)+1)
    astar_pathLength = textLabel(myMaze, "Astar PathLength ", len(astar_forwardPath)+1)
    policyI_pathLength = textLabel(myMaze, "MDP-PolicyIter PathLength ", len(policyI_forwardPath)+1)
    valueI_pathLength = textLabel(myMaze, "MDP-ValueIter PathLength ", len(valueI_forwardPath)+1)

    #time
    #bfs_time = textLabel(myMaze, "BFS timetaken: ", timeit(stmt = "BFS(myMaze)", number = 10, globals = globals()))
    #dfs_time = textLabel(myMaze, "DFS timetaken: ", timeit(stmt = "DFS(myMaze)", number = 10, globals = globals()))
    #astar_time = textLabel(myMaze, "Astar timetaken: ", timeit(stmt = "Astar(myMaze)", number = 10, globals = globals()))
    #policyI_time = textLabel(myMaze, "MDP-PolicyIter timetaken: ", timeit(stmt = "run_policy_iteration(myMaze)", number = 10, globals = globals()))
    #valueI_time = textLabel(myMaze, "MDP-ValueIter timetaken: ", timeit(stmt = "run_value_iteration(myMaze)", number = 10, globals = globals()))

    #memory
    bfs_memory = memory_usage((BFS, (myMaze,)))
    dfs_memory = memory_usage((DFS, (myMaze,)))
    astar_memory = memory_usage((Astar, (myMaze,)))
    policyI_memory_usage = memory_usage((run_policy_iteration, (myMaze,), {}))
    valueI_memory_usage = memory_usage((run_value_iteration, (myMaze,), {}))

    bfs_memory_label = textLabel(myMaze, "BFS max memory usage: ", f"{max(bfs_memory):.2f} MB")
    dfs_memory_label = textLabel(myMaze, "DFS max memory usage: ", f"{max(dfs_memory):.2f} MB")
    astar_memory_label = textLabel(myMaze, "Astar max memory usage: ", f"{max(astar_memory):.2f} MB")
    policyI_memory = textLabel(myMaze, "MDP-PolicyIter memory usage: ", f"{max(policyI_memory_usage):.2f} MB")
    valueI_memory = textLabel(myMaze, "MDP-ValueIter memory usage: ", f"{max(valueI_memory_usage):.2f} MB")

    myMaze.run()
