import random
import json



def addRandomNode(start, size, edges):
    node = {}
    node["title"] = "title" + str(start)
    node["found"] = False
    node["edges"] = []

    ##select random number of edged
    numEdges = random.randint(0, edges)
    for i in range(numEdges):
        edge = str(random.randint(0, size-1))
        while edge in node["edges"] or edge == str(start):
            edge = str(random.randint(0, size-1))
        node["edges"].append(edge)
    return node

def randomGraph():
    random.seed()
    testNum = random.randint(0, 10000)

    ##initiate graph
    graph = {}
    graph["start"] = ""
    graph["URLs"] = {}
    graph["cookie"] = 'test' + str(testNum)
    
    size = int(raw_input("Enter number of nodes in graph: "))
    if size == 0:
        return json.dumps(graph, indent=4, sort_keys=True)
    else:
        graph["start"] = str(random.randint(0, size - 1))

    edges = int(raw_input("Enter maximum number of edges per node: "))
    if edges > size:
        print "Error, more edges than nodes."
        return

    ## add nodes to json
    for i in range(size):
        graph["URLs"][i] = addRandomNode(i, size, edges)

    return json.dumps(graph)

def addNode(start, size):
    node = {}
    node["title"] = "title" + str(start)
    node["edges"] = []

    numEdges = int(raw_input("Enter number of edges for node " + str(start) + ": "))
    for i in range(numEdges):
        edge = raw_input("Enter edge number " + str(i) + " (range 0-" + str(size-1) + "): ")
        node["edges"].append(edge)

    resp = raw_input("Was the keyword found on this node (y/n): ")
    if resp == 'y' or resp == 'Y':
        node['found'] = True
    else:
        node['found'] = False
    return node
    
def createGraph():
    ##initiate graph
    unit = raw_input("Enter name of test for cookie: ")
    graph = {}
    graph["start"] = ""
    graph["URLs"] = {}
    graph["cookie"] = unit

    size = int(raw_input("Enter number of nodes in graph: "))
    if size == 0:
        return json.dumps(graph, indent=4, sort_keys=True)
    else:
        graph["start"] = "0"

    for i in range(size):
        graph["URLs"][int(i)] = addNode(i, size)

    return json.dumps(graph)
    
def main():
    random.seed()
    again = "y"
    while again == "y" or again == "Y":
        print "Select the type of graph you want to create:"
        print "1) Manually create graph"
        print "2) Create a random graph"
        choice = raw_input("> ")
        print ""
        if choice == "1":
            print createGraph()
        elif choice == "2":
            print randomGraph()
        print "Continue? (Y/y)"
        again = raw_input("> ")

main()
