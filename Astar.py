#Astar, informed heuristic search algorithm
#f(n) - cost of the cell
#g(n) - cost of the path from start node to n node (number of steps taken from start to n)
#h(n) - estimated cost to reach to the goal node from n node (estiamted number of steps taken from n to goal)

from pyMaze import maze, agent, COLOR, textLabel
import time
from queue import PriorityQueue
from timeit import timeit

def ManhattanDist(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def Astar(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    aStarSearch=[start]
    aStarPath = {}
    gn = {row: float("inf") for row in m.grid}
    gn[start] = 0
    fn = {row: float("inf") for row in m.grid}
    fn[start] = ManhattanDist(start, m._goal)	
	
    pq = PriorityQueue()
    pq.put((ManhattanDist(start, m._goal), ManhattanDist(start, m._goal), start))
	
    
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


    forwardPath={}
    cell=m._goal
    while cell!=start:
        forwardPath[aStarPath[cell]]=cell
        cell=aStarPath[cell]
    return aStarSearch,aStarPath,forwardPath

if __name__ == '__main__':
    #start_time = time.time()
    m = maze(30, 30)
    m.CreateMaze(loadMaze="maze--2023-03-09--11-37-25.csv") # loop percentage = 80% 

    searchSpace, reversePath, forwardPath = Astar(m)

    a = agent(m, footprints=True, shape='square', color = COLOR.yellow)
    b = agent(m, footprints=True, filled=True, color=COLOR.green)

    m.tracePath({a:searchSpace}, showMarked=True, delay = 20)
    m.tracePath({b:forwardPath}, delay = 50)

    #elapsed_time = time.time() - start_time
    AstarTime = timeit(stmt = "Astar(m)", number = 10, globals = globals())
    time = textLabel(m, "Timetaken to solve the 30X30 maze, using A star algorithm: ", AstarTime)
    pathLength = textLabel(m, "Length of the path ", len(forwardPath)+1)
    searchSpace = textLabel(m, "Total cells searched ", len(searchSpace)+1)
    m.run()

