import copy, heapq

open = []
close = []
children = []

def generate_children(curr_state):
    for i in range(3):
        if len(curr_state[i]):
            temp_copy = copy.deepcopy(curr_state)
            current_elm = temp_copy[i].pop()
            for j in range(3):
                if j!=i:
                    temp_next = copy.deepcopy(temp_copy)
                    temp_next[j].append(current_elm)
                    if temp_next not in open and temp_next not in close:
                        children.append(temp_next)

initial_state = [['A'], ['B', 'C'], []]
goal_state = [[], [], ['A', 'B', 'C']]

depth_limit = 0
curr_depth = 0

goal_depth = -1

open.append([initial_state, 0])

while True:
    while len(open):
        curr_state, curr_depth = open.pop()
        close.append(curr_state)
        
        if curr_state==goal_state:
            close.append(goal_state)
            break

        if curr_depth==depth_limit:
            continue
        
        generate_children(curr_state)
        while len(children):
            open.append([children.pop(), curr_depth+1])
    
    if close[-1]==goal_state:
        goal_depth = depth_limit
        break
    else:
        close.clear()
        open = [[initial_state, 0]]
        depth_limit += 1

if goal_depth!=-1:
    print('Goal Depth: ', goal_depth)
else:
    print('Goal not found', depth_limit)

print(close)
