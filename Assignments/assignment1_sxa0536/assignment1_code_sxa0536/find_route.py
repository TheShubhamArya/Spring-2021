# Shubham Arya 1001650536
# Uniform cost Search for uninformed
# A* for informed cost search
import sys
from graph import *
from queue import *

# I am using UCS to perform uninformed search using uniformed cost search.
# To implement UCS, I use priority queue to get the lowest cumulative cost
# For the informed search, I will be using A* algorithm.
# The function remains the same except in this f(n) = g(n) + h(n) where h(n) is the heuristic
# Note: I also keep track of what nodes have been visited otherwise it would fall into an infinite loop.
def find_route(graph, start, goal):

    queue = Queue()
    reached_goal = False
    total_cost_goal = 0
    nodes_expanded_counter = 0
    nodes_generated_counter = 0
    visited_locations = []
    h_cost_of_successors = {}

    successors = graph.getSuccessors(start) # The first successor is chosen as the start state
    visited_locations.append(start) # Add start to visited locations

    # adds successor to the queue with it's cost.
    for successor in successors:
        visited_locations.append(successor)
        nodes_generated_counter = nodes_generated_counter + 1
        cost = graph.getEdgeCost(start, successor)
        queue.insert((successor, cost), cost)

    while len(queue.queue) != 0:
        # sort the queue and remove the item from top. If that is the goal, end the while loop.
        current_node, cost_node = queue.remove()
        nodes_expanded_counter = nodes_expanded_counter + 1

        if current_node == goal:
            reached_goal = True
            total_cost_goal = cost_node
            break

        # get all successors of the current_node to see if we can reach the destination
        # if node has a successor then insert the successor into the queue and calculate total cost
        successors = graph.getSuccessors(current_node)
        h_cost_of_successors.clear()

        for successor in successors:
            if not heuristic_present:
                nodes_generated_counter = nodes_generated_counter + 1
                if successor not in visited_locations:
                    visited_locations.append(successor)
                    total_cost = graph.getEdgeCost(current_node, successor) + cost_node
                    queue.insert((successor, total_cost), total_cost)

            else:
                h_cost = graph.getEdgeCost(current_node, successor) + heuristic(successor)
                h_cost_of_successors[successor] = h_cost

                if successor not in visited_locations:
                    nodes_generated_counter = nodes_generated_counter + 1
                    visited_locations.append(successor)
                    total_cost = graph.getEdgeCost(current_node, successor) + cost_node
                    queue.insert((successor, total_cost), total_cost)
                    queue.sort()
    output(finish=reached_goal, expanded=nodes_expanded_counter, generated=nodes_generated_counter,
           cost=total_cost_goal)

# displays the output with the numbers of nodes generated, expanded, distance, and route.
def output(finish, expanded, generated, cost):
    print("nodes expanded: " + str(expanded))
    print("nodes generated: " + str(generated))
    if not finish:
        print("distance: infinity")
        print("route: none")
    else:
        print("distance: " + str(cost))
        print("route: " + sys.argv[2] + " -> " + sys.argv[3])

# opens the heuristic file and returns the weight of the node that matches with the current node
def heuristic(current_node):
    if not heuristic_present:
        return 0
    else:
        with open(sys.argv[4], "r") as file:
            for line in file:
                data = line.split(" ", 1)
                if line == 'END OF INPUT':
                    break
                if data[0] == current_node:
                    return float(data[1])
        return 0

heuristic_present = False

if __name__ == "__main__":

    graph = Graph()
    locations = []
    unique_locations = []

    if len(sys.argv) == 4:
        heuristic = 0
    elif len(sys.argv) == 5:
        heuristic_present = True
    else:
        print(
            "\nIncorrect number of arguments. Run with the command:\npython find_route.py input.txt origin destination "
            "h_dest.txt [optional]\n")
        exit(0)

    # This puts all possible locations in the locations array including duplicates
    with open(sys.argv[1], "r") as file:
        for line in file:
            data = line.split(" ", 2)
            if line == 'END OF INPUT':
                break
            locations.append(data[0])
            locations.append(data[1])

    # this filters out duplicate locations and put in a new unique_locations array
    for location in locations:
        if location not in unique_locations:
            unique_locations.append(location)

    # add each location as a node in the graph.
    for location in unique_locations:
        graph.addNode(location)

    # This parses through each line to filter locations and costs in separate variable.
    # This then connects the locations in the graph in an undirected way.
    with open(sys.argv[1], "r") as file:
        for line in file:
            data = line.split(" ", 2)
            if line == 'END OF INPUT':
                break
            # connection made twice so that it is undirected
            graph.connect(data[1], data[0], float(data[2]))
            graph.connect(data[0], data[1], float(data[2]))

    # checks if the start and destination from command line exists.
    if sys.argv[2] not in graph.getNodes():
        print("Start location " + sys.argv[2] + " does not exist")
    elif sys.argv[3] not in graph.getNodes():
        print("Destination location " + sys.argv[3] + " does not exist")
    elif sys.argv[2] == sys.argv[3]:
        print("nodes expanded: 0")
        print("nodes generated: 0")
        print("distance: 0")
        print("route: " + sys.argv[2])
    else:
        # calls the function to find distance between the two command line parameters in the graph just created.
        find_route(graph=graph, start=sys.argv[2], goal=sys.argv[3])
