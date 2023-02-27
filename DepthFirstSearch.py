from tkinter import CURRENT
from pyMaze import maze, agent, COLOR, textLabel
import time


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
        poss = 0
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
                dfsPath[childCell]=currentCell
        if poss>1:
            m.markCells.append(currentCell)
    forwardPath = {}
    cell = m._goal
    while cell != start:
        forwardPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    elapsed_time = time.time() - start_time
    return dfsSearch, dfsPath, forwardPath#, elapsed_time


if __name__ == '__main__':
    start_time = time.time()
    m = maze(20, 20)
    m.CreateMaze(loadMaze='maze--2023-02-27--10-57-01.csv') # loop percentage = 50% 
    # print(f"open and close grid paths in the maze are {m.maze_map}")
    searchSpace, reversePath, forwardPath = DFS(m)
    a = agent(m, footprints=True, shape='square', color = COLOR.blue)
    b = agent(m, 1, 1, goal=(20, 20), footprints=True, filled=True, color = COLOR.cyan)
    c = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({a:searchSpace}, showMarked=True)
    m.tracePath({b:reversePath})
    m.tracePath({c:forwardPath})
    elapsed_time = time.time() - start_time
    time = textLabel(m, "Timetaken to solve the 20X20 maze, using DFS algorithm is ", elapsed_time)
    #print(f"timetaken to solve the 20X20 maze, using DFS algorithm is {time_taken}")

    m.run()