from BreadthFirstSearch import BFS
from DepthFirstSearch import DFS 
from Astar import Astar, ManhattanDist
from pyMaze import *
from timeit import timeit
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

if __name__ == '__main__':
    myMaze = maze(30, 30)
    myMaze.CreateMaze(loadMaze="maze--2023-03-09--11-37-25.csv") # loop percentage = 80% 

    bfs_searchSpace, bfs_reversePath, bfs_forwardPath = BFS(myMaze)
    dfs_searchSpace, dfs_reversePath, dfs_forwardPath = DFS(myMaze)
    astar_searchSpace, astar_reversePath, astar_forwardPath = Astar(myMaze)
    
    agent_BFS = agent(myMaze, footprints=True, shape='square', filled=True,color = COLOR.green)
    agent_DFS = agent(myMaze, footprints=True, shape='square', filled=True, color = COLOR.blue)
    agent_Astar = agent(myMaze, footprints=True, shape='square', color = COLOR.yellow)

    myMaze.tracePath({agent_BFS:bfs_forwardPath}, delay=100)
    myMaze.tracePath({agent_DFS:dfs_forwardPath}, delay=100)
    myMaze.tracePath({agent_Astar:astar_forwardPath}, delay=100)

    #path length
    bfs_pathLength = textLabel(myMaze, "BFS PathLength ", len(bfs_forwardPath)+1)
    dfs_pathLength = textLabel(myMaze, "DFS PathLength ", len(dfs_forwardPath)+1)
    astar_pathLength = textLabel(myMaze, "Astar PathLength ", len(astar_forwardPath)+1)

    #time
    #bfs_time = textLabel(myMaze, "BFS timetaken: ", timeit(stmt = "BFS(myMaze)", number = 10, globals = globals()))
    #dfs_time = textLabel(myMaze, "DFS timetaken: ", timeit(stmt = "DFS(myMaze)", number = 10, globals = globals()))
    #astar_time = textLabel(myMaze, "Astar timetaken: ", timeit(stmt = "Astar(myMaze)", number = 10, globals = globals()))

    #memory
    bfs_memory = memory_usage((BFS, (myMaze,)))
    dfs_memory = memory_usage((DFS, (myMaze,)))
    astar_memory = memory_usage((Astar, (myMaze,)))

    #plt.plot(bfs_memory, label='BFS')
    #plt.plot(dfs_memory, label='DFS')
    #plt.plot(astar_memory, label='Astar')
    #plt.xlabel('Time (s)')
    #plt.ylabel('Memory usage (MiB)')
    #plt.title('Memory usage over time')
    #plt.legend()
    #plt.show()

    #plt.savefig("../memory_usage_plot.png")

    bfs_memory_label = textLabel(myMaze, "BFS max memory usage: ", f"{max(bfs_memory):.2f} MB")
    dfs_memory_label = textLabel(myMaze, "DFS max memory usage: ", f"{max(dfs_memory):.2f} MB")
    astar_memory_label = textLabel(myMaze, "Astar max memory usage: ", f"{max(astar_memory):.2f} MB")

    myMaze.run()



