
V = {'a', 'b', 'c', 'd', 'e'}		# 节点集
E = {'ab', 'ac', 'bd', 'cd', 'de'}	# 边集

class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        
# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

# Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
           self.gdict[vrtx] = []
                    

# Add the new edge
    def AddEdge(self, edge):
        if(edge[1] not in self.gdict[edge[0]]):
            self.gdict[edge[0]].append(edge[1])
        if(edge[0] not in self.gdict[edge[1]]):
            self.gdict[edge[1]].append(edge[0])


# List the edge names
    def findedge(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
        
    def edge(self):
        return self.findedge()
        
# Create the dictionary with graph elements
graph_elements = {
				"a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)
g.AddEdge(['a','e'])
g.AddEdge(['a','c'])
print(g.gdict)
print(g.edge())
