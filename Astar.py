from pyMaze import maze, agent, COLOR, textLabel
import time
from queue import PriorityQueue
from timeit import timeit
from memory_profiler import memory_usage

import math

def EuclideanDist(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def DiagonalDist(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return dx + dy + (math.sqrt(2) - 2) * min(dx, dy)

def ManhattanDist(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def Astar(m,start=None, heuristics = "Manhattan"):
    if start is None:
        start=(m.rows,m.cols)
    aStarSearch=[start]
    aStarPath = {}
    gn = {row: float("inf") for row in m.grid}
    gn[start] = 0
    fn = {row: float("inf") for row in m.grid}

    if heuristics is "Manhattan":
        fn[start] = ManhattanDist(start, m._goal)	

    if heuristics is "Euclidean":
        fn[start] = EuclideanDist(start, m._goal)

    if heuristics is "Diagonal":
        fn[start] = DiagonalDist(start, m._goal)
	
    pq = PriorityQueue()

    pq.put((ManhattanDist(start, m._goal), ManhattanDist(start, m._goal), start))

    if heuristics is "Manhattan":
        pq.put((ManhattanDist(start, m._goal), ManhattanDist(start, m._goal), start))

    if heuristics is "Euclidean":
        pq.put((EuclideanDist(start, m._goal), EuclideanDist(start, m._goal), start))

    if heuristics is "Diagonal":
        pq.put((DiagonalDist(start, m._goal), DiagonalDist(start, m._goal), start))
	
    
    while not pq.empty():
        currentCell = pq.get()[2]
        aStarSearch.append(currentCell)
        if currentCell == m._goal:
            break        
        for d in 'ESNW':
            if m.maze_map[currentCell][d] == True:
                if d == 'E':
                    childCell = (currentCell[0], currentCell[1]+1)
                elif d == 'W':
                    childCell = (currentCell[0], currentCell[1]-1)
                elif d == 'S':
                    childCell = (currentCell[0]+1, currentCell[1])
                elif d == 'N':
                    childCell = (currentCell[0]-1, currentCell[1])
                
                temp_gn = gn[currentCell] + 1
                temp_fn = temp_gn + ManhattanDist(childCell, m._goal)

                if temp_fn < fn[childCell]:   
                    aStarPath[childCell] = currentCell
                    gn[childCell] = temp_gn
                    fn[childCell] = temp_gn + ManhattanDist(childCell, m._goal)
                    pq.put((fn[childCell], ManhattanDist(childCell, m._goal), childCell))

                if heuristics is "Manhattan":
                    temp_gn = gn[currentCell] + 1
                    temp_fn = temp_gn + ManhattanDist(childCell, m._goal)

                    if temp_fn < fn[childCell]:   
                        aStarPath[childCell] = currentCell
                        gn[childCell] = temp_gn
                        fn[childCell] = temp_gn + ManhattanDist(childCell, m._goal)
                        pq.put((fn[childCell], ManhattanDist(childCell, m._goal), childCell))

                if heuristics is "Euclidean":
                    temp_gn = gn[currentCell] + 1
                    temp_fn = temp_gn + EuclideanDist(childCell, m._goal)

                    if temp_fn < fn[childCell]:   
                        aStarPath[childCell] = currentCell
                        gn[childCell] = temp_gn
                        fn[childCell] = temp_gn + EuclideanDist(childCell, m._goal)
                        pq.put((fn[childCell], EuclideanDist(childCell, m._goal), childCell))

                if heuristics is "Diagonal":
                    temp_gn = gn[currentCell] + 1
                    temp_fn = temp_gn + DiagonalDist(childCell, m._goal)

                    if temp_fn < fn[childCell]:   
                        aStarPath[childCell] = currentCell
                        gn[childCell] = temp_gn
                        fn[childCell] = temp_gn + DiagonalDist(childCell, m._goal)
                        pq.put((fn[childCell], DiagonalDist(childCell, m._goal), childCell))


    forwardPath={}
    cell=m._goal
    while cell!=start:
        forwardPath[aStarPath[cell]]=cell
        cell=aStarPath[cell]
    return aStarSearch,aStarPath,forwardPath

if __name__ == '__main__':
    #start_time = time.time()
    m = maze()
    m.CreateMaze(loadMaze="maze--2023-03-12--09-33-14.csv") # loop percentage = 80% 

    searchSpace, reversePath, forwardPath = Astar(m, heuristics="Manhattan")

    a = agent(m, footprints=True, shape='square', color = COLOR.yellow)
    b = agent(m, footprints=True, filled=True, color=COLOR.green)

    m.tracePath({a:searchSpace}, showMarked=True, delay = 20)
    m.tracePath({b:forwardPath}, delay = 50)

    #elapsed_time = time.time() - start_time
    AstarTime = timeit(stmt = "Astar(m)", number = 10, globals = globals())
    #time = textLabel(m, "Timetaken: ", AstarTime)
    #pathLength = textLabel(m, "Length of the path ", len(forwardPath))
    #searchSpace = textLabel(m, "Total cells searched ", len(searchSpace))

    astar_memory = memory_usage((Astar, (m,), {'heuristics': 'Manhattan'}))

    #astar_memory_label = textLabel(m, "Astar memory: ", f"{max(astar_memory):.2f} MB")

    m.run()

