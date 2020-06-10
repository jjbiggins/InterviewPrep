from basicgraph import *

# core of classic Depth First Search
#
# See e.g. http://en.wikipedia.org/wiki/Depth-first_search
#
def recDFS(graph, startNode):
    print("processing:", startNode.name)
    startNode.setStatus('processed')
    for node in graph.neighborsOf(startNode):
        if node.getStatus() == 'unseen':
            node.setStatus('seen')
            recDFS(graph, node)
        
# driver for classic Depth First Search
#
def dfs(graph, startNode):
    for n in graph.nodes:
        n.setStatus('unseen')
    recDFS(graph, startNode)
