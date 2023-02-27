from tkinter import CURRENT
from pyMaze import maze, agent, COLOR, textLabel
import time

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
                if d == 'E':
                    childCell = (currentCell[0], currentCell[1]+1)
                elif d == 'W':
                    childCell = (currentCell[0], currentCell[1]-1)
                elif d == 'S':
                    childCell = (currentCell[0]+1, currentCell[1])
                elif d == 'N':
                    childCell = (currentCell[0]-1, currentCell[1])
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
    start_time = time.time()
    m = maze(20, 20)
    m.CreateMaze(loadMaze='maze--2023-02-27--10-57-01.csv') # loop percentage = 50% 
    searchSpace, reversePath, forwardPath = BFS(m)
    a = agent(m, footprints=True, shape='square', color = COLOR.blue)
    b = agent(m, 1, 1, goal=(20, 20), footprints=True, filled=True, color = COLOR.cyan)
    c = agent(m, footprints=True, color=COLOR.yellow)
    m.tracePath({a:searchSpace}, showMarked=True)
    m.tracePath({b:reversePath})
    m.tracePath({c:forwardPath})
    elapsed_time = time.time() - start_time
    time = textLabel(m, "Timetaken to solve the 20X20 maze, using BFS algorithm is ", elapsed_time)
    pathLength = textLabel(m, "Length of the path ", len(forwardPath)+1)
    searchSpace = textLabel(m, "Total cells searched ", len(searchSpace)+1)
    m.run()
