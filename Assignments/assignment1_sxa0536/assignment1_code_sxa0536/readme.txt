Shubham Arya 1001650536

Language- Python 3.0+. Did not run it on omega.

Structure- 
	The code has 4 files in it. The main file is find_route.py. this file contains the code that is responsible for getting and setting information from the command line. This is also where the output is set

	priority_queue.py inserts, remove, sort or check for empty queue items. I use a queue to keep track of the lowest cumulative cost that is possible. These functions are called in the find_route.py file.

	graph.py graphs the nodes by connecting them together. It also adds the nodes to the graph and is used to find the edge cost and the successors for a node. 

	nodes.py contains information specifically about a node. It stores the successors, the cost of the successors and the key value of the node itself. 

Instructions- 

To run the code on your command line, you need to first locate the code on the terminal. Once you are on this assignments directory, follow the steps.
Type-
	python find_route.py input_filename.txt start destination h_file.txt [optional].

Here input_filename.txt is the file with the data for the graph. Start is the start location and destination is the goal.
h_file.txt is an optional argument. This is the heuristic file if used, will use the A* search. otherwise it will use the UCS.
Note: Everything is case sensitive so make sure it is typed as it is.

References:
https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/
https://steemit.com/algorithm/@vamshikshetty/uniform-cost-search-for-graph
https://www.redblobgames.com/pathfinding/a-star/implementation.html
https://www.youtube.com/watch?v=dRMvK76xQJI