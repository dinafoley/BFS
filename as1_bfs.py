#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right, 
#Points: 2
def traverse(tree, init):    	
	queue = [init]
	traversed = []
	while queue:
		'''
			Student fixes the loopy path from here to the end of this function
		'''
		node = queue.pop(0)
		if node not in traversed:
			traversed.append(node)

		leaves = tree[node]
		for leaf in leaves:
			if leaf not in traversed:
				queue.append(leaf)

	return traversed

#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [[init]]
	if init == goal:
		return "No kidding, pls"

	while queue:
		'''
				You implement the path finder from here
		'''
		# popping path
		path = queue.pop(0)
		node = path[-1]
		if node not in traversed:
			leaves = tree[node]
			for leaf in leaves:
				test_path = list(path)
				test_path.append(leaf)
				queue.append(test_path)
				if leaf == goal:
					goal_path = test_path
					return goal_path
			traversed.append(node)
	return "No such path exists"

