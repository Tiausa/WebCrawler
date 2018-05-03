import random
import json



def addNode(start, size, edges):
    node = {}
    node["title"] = "title" + str(start)
    node["found"] = 0
    node["edges"] = []

    ##select random number of edged
    numEdges = random.randint(0, edges)
    for i in range(numEdges):
        edge = random.randint(0, size)
        while edge in node["edges"]:
            edge = random.randint(0, size)
        node["edges"].append(edge)
    return node

def randomGraph():
    random.seed(0)
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
        graph["start"] = random.randint(0, size - 1)

    edges = int(raw_input("Enter maximum number of edges per node: "))
    if edges > size:
        print "Error, more edges than nodes."
        return

    ## add nodes to json
    for i in range(size):
        graph["URLs"][i] = addNode(i, size, edges)

    return json.dumps(graph, indent=4, sort_keys=True)
        

print randomGraph()
