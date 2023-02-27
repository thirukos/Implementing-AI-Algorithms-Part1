# maze generated using recursive backtracker
# by default it creates perfect maze - only one path from start to goal, loopPercent can be set to increase the number of loops
# by default it creates 10 rows and 10 columns maze
# by default (1,1) is the start cell, but can be changed in CreateMaze function

from pyMaze import maze, COLOR, agent, textLabel

m = maze()
# saveMaze = True, generated maze as csv file
# loadMaze = "xxx.csv" 
m.CreateMaze()
a = agent(m, footprints=True)
#print(a.x)
#print(a.y)
#print(a.position)
print(m.grid)

# m.enableArrowKey(a) - to use arraow keys to move the agent

#m.tracePath({a: m.path}, delay=100, ) #shortest path solution 

m.run()