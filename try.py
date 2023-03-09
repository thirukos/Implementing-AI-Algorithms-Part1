import numpy as np
from pyMaze import maze, agent, COLOR, textLabel

'''==================================================
Initial set up
=================================================='''

l = 20
b = 20
maze_obj = maze(l, b)
maze_obj.CreateMaze(loadMaze='maze--2023-02-27--10-57-01.csv')

#Hyperparameters
SMALL_ENOUGH = 0.005
GAMMA = 0.9         
NOISE = 0.10  

#Define all states
all_states=[]
for i in range(1,l+1):
    for j in range(1,b+1):
            all_states.append((i,j))

#all_states = list(m.maze_maps.keys())

#Define rewards for all states
rewards = {}
for i in all_states:
    if i == (1,1):
        rewards[i] = 1000
    else:
        rewards[i] = -1

#Dictionnary of possible actions. We have two "end" states (1,2 and 2,2)
actions = {}

#can be changed
for i in range(1,l+1):
    for j in range(1,b+1):
        currCell = (i,j)
        actions[currCell] = ()
        for dir in 'NESW':
            if maze_obj.maze_map[currCell][dir]==True:
                if dir == 'N':
                    # childCell = (currCell[0]-1, currCell[1])
                    actions[currCell] += ('N',)
                elif dir == 'E':
                    # childCell = (currCell[0], currCell[1]+1)
                    actions[currCell] += ('E',)
                elif dir == 'S':
                    # childCell = (currCell[0]+1, currCell[1])
                    actions[currCell] += ('S',)
                elif dir == 'W':
                    # childCell = (currCell[0], currCell[1]-1)
                    actions[currCell] += ('W',)


# print(actions[(1,1)][0])


#Define an initial policy
policy={}
for s in actions.keys():
    policy[s] = np.random.choice(actions[s])

#Define initial value function 
V={}
for s in all_states:
    if s in actions.keys():
        V[s] = -1
    if s ==(1,1):
        V[s]= 10000
        
'''==================================================
Value Iteration
=================================================='''

iteration = 0

while True:
    biggest_change = 0
    for s in all_states:            
        if s in policy:
            
            old_v = V[s]
            new_v = 0
            
            for a in actions[s]:
                if a == 'N':
                    nxt = [s[0]-1, s[1]]
                if a == 'S':
                    nxt = [s[0]+1, s[1]]
                if a == 'W':
                    nxt = [s[0], s[1]-1]
                if a == 'E':
                    nxt = [s[0], s[1]+1]

                #Calculate the value
                nxt = tuple(nxt)
                # act = tuple(act)
                v = rewards[s] + (GAMMA * V[nxt])
                # v = rewards[s] + (GAMMA * ((1-NOISE)* V[nxt] + (NOISE * V[act]))) 
                if v > new_v: #Is this the best action so far? If so, keep it
                    new_v = v
                    policy[s] = a

       #Save the best of all actions for the state                                
            V[s] = new_v
            biggest_change = max(biggest_change, np.abs(old_v - V[s]))

            
   #See if the loop should stop now         
    if biggest_change < SMALL_ENOUGH:
        break
    iteration += 1



fnlPath = []
# print(policy)

strt = (l,b)
fnlPath.append(strt)

while True:
    dir = policy[strt]
    if dir == 'N':
        strt = (strt[0]-1, strt[1])
    if dir == 'E':
        strt = (strt[0], strt[1]+1)
    if dir == 'S':
        strt = (strt[0]+1, strt[1])
    if dir == 'W':
        strt = (strt[0], strt[1]-1)

    fnlPath.append(strt)

    if strt == (1,1):
        break

a = agent( maze_obj, footprints=True, color = COLOR.green)
maze_obj.tracePath({a:fnlPath}, delay=50)



maze_obj.run()

