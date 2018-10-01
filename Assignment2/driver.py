#by Mengyao Li (ml4042)
import time
import resource
import sys
from collections import OrderedDict
from operator import itemgetter



goalState = [0,1,2,3,4,5,6,7,8]


class Node:
	def __init__(self, state, action, depth, parent, cost):
		self.state = state
		self.action=action
		self.depth=depth
		self.parent=parent
		self.cost=cost


def find_neighbors(node):
	po = node.state.index(0)
	#print(po)
	neighbors = []
	newnode0 = Node(None, None, 0, None, 0)
	newnode1 = Node(None, None, 0, None, 0)
	newnode2 = Node(None, None, 0, None, 0)
	newnode3 = Node(None, None, 0, None, 0)
	#print("newnode type",type(newnode))


	if po == 0:
		newnode0.state = down(node.state,po)
		newnode0.action = "Down"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1
		#newnode0 = (down(node.state,po),"down",node.depth+1,node,node.cost+1)

		neighbors.append(newnode0)

		newnode1.state = right(node.state,po)
		newnode1.action = "Right"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1


		neighbors.append(newnode1)


	if po == 2:
		newnode0.state = down(node.state,po)
		newnode0.action = "Down"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1

		neighbors.append(newnode0)

		newnode1.state = left(node.state,po)
		newnode1.action = "Left"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1

		neighbors.append(newnode1)


	if po == 6:
		newnode0.state = up(node.state,po)
		newnode0.action = "Up"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1

		neighbors.append(newnode0)

		newnode1.state = right(node.state,po)
		newnode1.action = "Right"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1

		neighbors.append(newnode1)


	if po == 8:
		newnode0.state = up(node.state,po)
		newnode0.action = "Up"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1

		neighbors.append(newnode0)

		newnode1.state = left(node.state,po)
		newnode1.action = "Left"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1

		neighbors.append(newnode1)


	if po == 1:
		newnode0.state = down(node.state,po)
		newnode0.action = "Down"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1

		neighbors.append(newnode0)

		newnode1.state = right(node.state,po)
		newnode1.action = "Right"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1

		neighbors.append(newnode1)

		newnode2.state = left(node.state,po)
		newnode2.action = "Left"
		newnode2.depth = node.depth+1
		newnode2.parent = node
		newnode2.cost = node.cost+1

		neighbors.append(newnode2)
		#print("1newnode type",type(newnode))

	if po == 7:
		newnode0.state = up(node.state,po)
		newnode0.action = "Up"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1

		neighbors.append(newnode0)

		newnode1.state = right(node.state,po)
		newnode1.action = "Right"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1

		neighbors.append(newnode1)

		newnode2.state = left(node.state,po)
		newnode2.action = "Left"
		newnode2.depth = node.depth+1
		newnode2.parent = node
		newnode2.cost = node.cost+1

		neighbors.append(newnode2)
		#print("7newnode type",type(newnode))

	if po == 3:
		newnode0.state = up(node.state,po)
		newnode0.action = "Up"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1

		neighbors.append(newnode0)

		newnode1.state = down(node.state,po)
		newnode1.action = "Down"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1

		neighbors.append(newnode1)

		newnode2.state = right(node.state,po)
		newnode2.action = "Right"
		newnode2.depth = node.depth+1
		newnode2.parent = node
		newnode2.cost = node.cost+1

		neighbors.append(newnode2)
		#print("3newnode type",type(newnode))

	if po == 5:
		newnode0.state = up(node.state,po)
		newnode0.action = "Up"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1
		#newnode0 = (up(node.state,po),"up",node.depth+1,node,node.cost+1)
		#print(newnode.state)
		neighbors.append(newnode0)
		#for m in neighbors:
			#print("neinow",m.state)

		newnode1.state = down(node.state,po)
		newnode1.action = "Down"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1


		neighbors.append(newnode1)
		#print(newnode1.state)
		#for m in neighbors:
			#print("neinow",m.state)

		newnode2.state = left(node.state,po)
		newnode2.action = "Left"
		newnode2.depth = node.depth+1
		newnode2.parent = node
		newnode2.cost = node.cost+1
		neighbors.append(newnode2)
		#print(newnode2.state)
		#for m in neighbors:
			#print("neinow",m.state)

		#print("5newnode type",type(newnode))
		#for m in neighbors:
			#print(m.state)


	if po == 4:
		newnode0.state = up(node.state,po)
		newnode0.action = "Up"
		newnode0.depth = node.depth+1
		newnode0.parent = node
		newnode0.cost = node.cost+1
		neighbors.append(newnode0)

		newnode1.state = down(node.state,po)
		newnode1.action = "Down"
		newnode1.depth = node.depth+1
		newnode1.parent = node
		newnode1.cost = node.cost+1

		neighbors.append(newnode1)

		newnode2.state = left(node.state,po)
		newnode2.action = "Left"
		newnode2.depth = node.depth+1
		newnode2.parent = node
		newnode2.cost = node.cost+1
		neighbors.append(newnode2)

		newnode3.state = right(node.state,po)
		newnode3.action = "Right"
		newnode3.depth = node.depth+1
		newnode3.parent = node
		newnode3.cost = node.cost+1
		neighbors.append(newnode3)
		#print("4newnode type",type(newnode))

	return neighbors

def down(state,po):
	statenew = state.copy()
	statenew[po+3], statenew[po] = statenew[po],statenew[po+3]
	#print(state)
	return statenew

def up(state,po):
	statenew = state.copy()
	statenew[po-3], statenew[po] = statenew[po],statenew[po-3]
	#print(state)
	return statenew

def left(state,po):
	statenew = state.copy()
	statenew[po-1], statenew[po] = statenew[po],statenew[po-1]
	#print(state)
	return statenew

def right(state,po):
	statenew = state.copy()
	statenew[po+1], statenew[po] = statenew[po],statenew[po+1]
	#print(state)
	return statenew

def goalTest(state):
	if state == goalState:
		return True

#print("initial state:",initialState)
#print("goal state:",goalState)

def bfs(initial):

	initialState = initial
	node = Node(initialState,None,0,None,0)
	#print(node.state)
	n = Node(None,None,0,None,0)

	frontier = []
	frontier.append(node)
	#print("initial frontier:",frontier[0])
	explored = set()

	frontier_state = set()
	frontier_state.add(tuple(initialState))


	neighbors = []
	expand=0
	max_depth=0

	while frontier:
		node = frontier.pop(0)
		explored.add(tuple(node.state))

		if goalTest(node.state) == True:

			path_to_goal = [node.action]
			noden = Node(None,None,0,None,0)
			noden = node
			while noden.parent.action != None:
				path_to_goal.append((noden.parent.action))
				noden=noden.parent
			path_to_goal.reverse()
			cost = len(path_to_goal)
			print("path_to_goal:",path_to_goal)
			print("cost_of_path:",cost)
			print("nodes_expanded:",expand)
			print("search depth:",node.depth)
			print("max_search_depth",max_depth)


			break

		neighbors = find_neighbors(node)
		expand = expand+1
		#expend = expend + 1

		for n in neighbors:
			#expend = expend +1

			if tuple(n.state) not in frontier_state and tuple(n.state) not in explored:
				frontier.append(n)
				frontier_state.add(tuple(n.state))
				max_depth = max(max_depth,n.depth)
	return False


def dfs(initial):
	initialState = initial
	node = Node(initialState,None,0,None,0)
	#print(node.state)
	n = Node(None,None,0,None,0)

	frontier = []
	frontier.append(node)
	#print("initial frontier:",frontier[0])
	explored = set()

	frontier_state = set()
	frontier_state.add(tuple(initialState))
 

	neighbors = []
	expand=0
	max_depth=0

	while frontier:
		node = frontier.pop()
		#print("node:",node.state)
		explored.add(tuple(node.state))

		if goalTest(node.state) == True:

			path_to_goal = [node.action]
			noden = Node(None,None,0,None,0)
			noden = node
			while noden.parent.action != None:
				path_to_goal.append((noden.parent.action))
				noden=noden.parent
			path_to_goal.reverse()
			print("path_to_goal:",path_to_goal)

			cost = len(path_to_goal)
			print("cost_of_path:",cost)
			print("nodes_expanded:",expand)
			print("search depth:",node.depth)			
			print("max_search_depth:",max_depth)
			

			break

		neighbors = find_neighbors(node)
		expand = expand+1
		#print(neighbors)
		neighbors.reverse()
		#print(neighbors)
		#x=reverse(neighbors)
		#print(x)

		for n in neighbors:
			#print("n",n.state)

			#expend = expend +1

			if tuple(n.state) not in frontier_state and tuple(n.state) not in explored:
				frontier.append(n)
				frontier_state.add(tuple(n.state))
				#print("frontier:",frontier_state)
				max_depth = max(max_depth,n.depth)

	return False
def h2(po1,po2):

    m = abs(po1 // 3 - po2 // 3) + abs(po1 % 3 - po2 % 3)
    return m

def h(state):
	dist = 0
	for i in range(0,8):
		dist = dist+h2(state.index(i),i)
	return dist


def sort_cost(frontier):

	dict = {}
	#print("dict:",dict)
	frontier_sort = []
	#dict_1={}
	#frontier_1=[]
	#print("frontier_sort:",frontier_sort)


	for n in frontier:
		cost = n.depth + h(n.state)
		#print("cost",cost)
		dict[n] = cost
		#print("diction:",dict)


	for key, value in sorted(dict.items(), key = itemgetter(1), reverse = False):
		#print("key:",key,value)
		frontier_sort.append(key)


	return frontier_sort





#print("initial state:",initialState)
#print("goal state:",goalState)

def ast(initial):
	initialState = initial
	node = Node(initialState,None,0,None,0)
	#print(node.state)
	n = Node(None,None,0,None,0)

	frontier = []
	frontier.append(node)
	#print("initial frontier:",frontier[0])
	explored = set()

	frontier_state = set()
	frontier_state.add(tuple(initialState))


	neighbors = []
	expand=0
	max_depth = 0

	while frontier:

		frontier = sort_cost(frontier)
		#print("frontier after:",frontier)
		node = frontier.pop(0)
		#print("node:",node.state)
		explored.add(tuple(node.state))

		if goalTest(node.state) == True:

			path_to_goal = [node.action]
			noden = Node(None,None,0,None,0)
			noden = node
			while noden.parent.action != None:
				path_to_goal.append((noden.parent.action))
				noden=noden.parent
			path_to_goal.reverse()
			print("path_to_goal:",path_to_goal)

			cost = len(path_to_goal)
			print("cost_of_path:",cost)
			print("nodes_expanded:",expand)
			print("search depth:",node.depth)			
			print("max_search_depth:",max_depth)



			
			break


		neighbors = find_neighbors(node)
		expand = expand+1
		#print(neighbors)


		for n in neighbors:
			#print("n",n.state)

			#expend = expend +1

			if tuple(n.state) not in frontier_state and tuple(n.state) not in explored:
				frontier.append(n)
				frontier_state.add(tuple(n.state))
				#print("frontier:",frontier_state)
				max_depth = max(max_depth,n.depth)

def main():

	#ini = map(int,sys.argv[2].split(','))

	starttime = time.time()

	#print(ini)
	#print (ini)
	#initial = sys.argv[2]
	#print(sys.argv[2])
	ini = sys.argv[2]
	inix = ini.split(",")   
	#print(inix)
	initial = []

	for i in range(0,len(inix)):
		#print(inix[i]) 
		initial.append(int(inix[i]))

	#print(initial)


	#print(initial)
	#initial = [1,2,5,3,4,0,6,7,8]
	if sys.argv[1] == 'bfs':
		bfs(initial)
	elif sys.argv[1] == 'dfs':
		dfs(initial)
	elif sys.argv[1] == 'ast':
		ast(initial)
	else:
		print("wrong input!")

	elapsedtime = time.time() - starttime
	print("running time:",elapsedtime)
	print("max_ram_usage:",(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)/(1024*1024))



if __name__ == "__main__":
    # execute only if run as a script
    main()



