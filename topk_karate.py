import networkx as nx
import tarjan
import itertools
G=nx.karate_club_graph()
#th = input('Threshold: ')
#print(th)
th =0.2

def strongly_connected_components(graph):
    """
    Tarjan's Algorithm (named for its discoverer, Robert Tarjan) is a graph theory algorithm
    for finding the strongly connected components of a graph.
    """

    index_counter = [0]
    stack = []
    lowlinks = {}
    index = {}
    result = []
    
    def strongconnect(node):
        # set the depth index for this node to the smallest unused index
        index[node] = index_counter[0]
        lowlinks[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
    
        # Consider successors of `node`
        try:
            successors = graph[node]
        except:
            successors = []
        for successor in successors:
            if successor not in lowlinks:
                # Successor has not yet been visited; recurse on it
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node],lowlinks[successor])
            elif successor in stack:
                # the successor is in the stack and hence in the current strongly connected component (SCC)
                lowlinks[node] = min(lowlinks[node],index[successor])
        
        # If `node` is a root node, pop the stack and generate an SCC
        if lowlinks[node] == index[node]:
            connected_component = []
            
            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node: break
            component = tuple(connected_component)
            # storing the result
            result.append(component)
    
    for node in graph:
        if node not in lowlinks:
            strongconnect(node)
    
    return result

score = []
#for v in G:
#	score.append(0)
res= strongly_connected_components(G)
#print(res)
#def updatescore(u,G)
	## find closely connected group Cu
#	Cu= strongly_connected_components(G)
#	c = Cu.nodes()
#	score[u] = 0
#	for c in Cu:
#		closeness[c,u]
#		if closeness[c,u] <0:
#			score[u] = score[u] -closeness[c,u]
#	return score[u]

#for G.edges() in G:
for (u, v) in G.edges():
	q = G.neighbors(u)
	w = G.neighbors(v)
	intersec = set(q).intersection(w)
	uni = set(q).union(w)
	asa = (len(intersec)*1.000/len(uni)*1.000)
	#print(asa)
    	G.add_edge(u,v,weight=asa)	

cq=34
N=0
closeness = []
for iv in range(34):
	closeness.append(0)
for v in G:
	for i in G.neighbors(v):
		
		if(G[v][i]['weight']!=0):
			N=N+1
		#	print(G.get_edge_data(v,i))
			closeness[v]+=G[v][i]['weight']
		#	print(G[v][i]['weight'])
	closeness[v] = (closeness[v] -(N*th))/cq 
	closeness[v] = -1 * closeness[v]
	print(closeness[v])
	N=0
	

gr =[[0 for x in range(2)] for y in range(34)] 
print("Node Degree")
for v in G:
    	gr[v][0] =v
	gr[v][1] = G.degree(v)
	print('%s %s' % (v,G.degree(v)))

q=sorted(gr)
print(q)	
