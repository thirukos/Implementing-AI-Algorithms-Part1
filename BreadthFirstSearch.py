from tkinter import CURRENT
from pyMaze import maze, agent, COLOR, textLabel
from timeit import timeit

def BFS(m, start_cell = None):
    if start_cell is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    bfsPath = {}
    bfsSearch = []
    while len(frontier)>0:
        currentCell = frontier.pop(0)
        bfsSearch.append(currentCell)
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
                bfsPath[childCell]=currentCell
    forwardPath = {}
    cell = m._goal
    while cell != start:
        forwardPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return bfsSearch, bfsPath, forwardPath

if __name__ == '__main__':
    #start_time = time.time()
    m = maze()
    m.CreateMaze(loadMaze="maze--2023-03-12--09-33-14.csv") # loop percentage = 80% 
    searchSpace, reversePath, forwardPath = BFS(m)

    a = agent(m, footprints=True, shape='square', color = COLOR.yellow)
    b = agent(m, footprints=True, filled=True, color =COLOR.green)

    m.tracePath({a:searchSpace}, showMarked=True, delay=50)
    m.tracePath({b:forwardPath}, delay=100)

    BFSTime = timeit(stmt = "BFS(m)", number = 10, globals = globals())
    #time = textLabel(m, "Timetaken to solve the 30X30 maze, using BFS algorithm: ", BFSTime)

    #pathLength = textLabel(m, "Length of the path ", len(forwardPath))
    #searchSpace = textLabel(m, "Total cells searched ", len(searchSpace))

    m.run()
