# maze generated using recursive backtracker
# by default it creates perfect maze - only one path from start to goal, loopPercent can be set to increase the number of loops
# by default it creates 10 rows and 10 columns maze
# by default (1,1) is the start cell, but can be changed in CreateMaze function

from pyMaze import maze, COLOR, agent, textLabel

m = maze()
# saveMaze = True, generated maze as csv file
# loadMaze = "xxx.csv" 
m.CreateMaze()
#a = agent(m, footprints=True)
#print(a.x)
#print(a.y)
#print(a.position)
#lastCell = list(m.maze_map.keys())
#print(lastCell)
#print(lastCell[0])
#mazeKeys = list(m.maze_map.keys())
#end = mazeKeys[0]
#print(end)

#for y in range(m.cols):
#    for x in range(m.rows):
#        if (x != end[0]) or (y != end[1]):
#            print(y)
#            print(x)
#        else:
#            print('ok')

#targetKey = m.maze_map[(7,1)]
cells = list(m.maze_map)
start_cell = list(m.maze_map.keys())[-1]
target_cell = list(m.maze_map.keys())[0]
print(start_cell)
print(target_cell)
print(m.maze_map[(4,4)])

actions = []
for direction, Bool in m.maze_map[(4,4)].items():
    if Bool ==1:
        actions.append(direction)
print(actions)

#print(m.maze_map[(1,1)])
#for direction,v in targetKey.items():
#    print(direction)
#    print(v)

# a deterministic policy should only have one possible action
#chosen_action = [key for (key, value) in targetKey.items() if value]
#assert len(chosen_action) == 1, f"actions = {chosen_action}"

# m.enableArrowKey(a) - to use arraow keys to move the agent

#m.tracePath({a: m.path}, delay=100, ) #shortest path solution 

#m.run()