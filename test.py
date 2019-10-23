def a_star(self, init, model, goal):
		goal = goal[0]
		init = init[0]
		vertex_init = Node(init, None)
		
		queue = PriorityQueue()
		queue.put(vertex_init, 0)
		vertex_init.father = None
		#came_from = {}
		#came_from[vertex_init.index] = None
		cost_so_far = [] * 114
		cost_so_far[vertex_init.index] = 0
		
		while not queue.empty():
			current = queue.get() #averiguar isto, acho que nao funciona bem
			
			if current.index == goal:
				break
			
			for neighbour in self.neighbors(current.index): #[transport, index]
				if next not in cost_so_far or new_cost < cost_so_far[next]:
					neighbour = Node(neighbour[1], current.index) 
					new_cost = cost_so_far[current.index] + 1
					cost_so_far[neighbour[1]] = new_cost
					priority = new_cost + heuristic(goal, neighbour)
					queue.put(neighbour, priority)

		return cost_so_far