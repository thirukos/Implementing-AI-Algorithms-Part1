from tkinter import CURRENT
from pyMaze import maze, agent, COLOR, textLabel
from timeit import timeit


def DFS(m, start_cell = None):
    #start_time = time.time()
    if start_cell is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    dfsSearch = []
    while len(frontier)>0:
        currentCell = frontier.pop()
        dfsSearch.append(currentCell)
        if currentCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currentCell][d] == True:
                if d == 'N':
                    childCell = (currentCell[0]-1, currentCell[1])
                elif d == 'E':
                    childCell = (currentCell[0], currentCell[1]+1)
                elif d == 'W':
                    childCell = (currentCell[0], currentCell[1]-1)
                elif d == 'S':
                    childCell = (currentCell[0]+1, currentCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currentCell
    forwardPath = {}
    cell = m._goal
    while cell != start:
        forwardPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    #elapsed_time = time.time() - start_time
    return dfsSearch, dfsPath, forwardPath


if __name__ == '__main__':
    #start_time = time.time()
    m = maze()
    m.CreateMaze(loadMaze="maze--2023-03-12--09-33-14.csv") # loop percentage = 80% 

    searchSpace, reversePath, forwardPath = DFS(m)

    a = agent(m, footprints=True, shape='square', color = COLOR.yellow)
    b = agent(m, footprints=True, filled=True, color=COLOR.green)

    m.tracePath({a:searchSpace}, showMarked=True, delay=50)
    m.tracePath({b:forwardPath}, delay=100)
    #elapsed_time = time.time() - start_time

    DFSTime = timeit(stmt = "DFS(m)", number = 10, globals = globals())
    #time = textLabel(m, "Timetaken to solve the 30X30 maze, using DFS algorithm is ", DFSTime)
    #pathLength = textLabel(m, "Length of the path ", len(forwardPath))

    #searchSpace = textLabel(m, "Total cells searched ", len(searchSpace))

    m.run()