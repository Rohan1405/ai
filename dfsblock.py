import copy, heapq

open = []
close = []
children = []

def clear_lists():
  open.clear()
  close.clear()
  children.clear()

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

open.append(initial_state)

while len(open):
    curr_state = open.pop()
    close.append(curr_state)
    
    if curr_state==goal_state:
        break
    
    generate_children(curr_state)
    while len(children):
        open.append(children.pop())

print(close)
 