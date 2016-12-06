'''
Given an undirected graph G, find the minimum spanning tree within G. A minimum 
spanning tree connects all vertices in a graph with the smallest possible total 
weight of edges. Your function should take in and return an adjacency list structured 
like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
'''

'''
Noted this is a MST problem, implement Prim's algorithm
'''
from heapq import heappush, heappop, heapify
import numpy as np 
from collections import defaultdict


def Question3(G):
	'''
	G is an adjacency list representing an undirected graph. 
	'''
	N = len(G) # the number of vertices in graph
	# randomly choose a vertext to start with
	if N == 1: return G
	source = G.keys()[0]
	X = [source]
	# initialize an empty dict for storage of selected edges
	T = defaultdict(list)
	# initialize a heap, heap has every vertex but source for now
	h = []
	source_edge_track = {} # if source vertex has multiple edge to another vertex, pick the smallest edge
	for edge in G[source]:
		if edge[0] not in source_edge_track.keys():
			source_edge_track[edge[0]] = [edge[1]]
		else:
			source_edge_track[edge[0]].append(edge[1])
	for i in source_edge_track.keys():
		heappush(h, (min(source_edge_track[i]), i))

	# for the vertices have no edge to source, put infinity in heap
	for v in G.keys():
		if v != source and v not in source_edge_track.keys():
			heappush(h, (np.inf, v))

	# start to iterate, add one edge to the MST, pop one vertex from h, for each iteration
	last = source
	while (len(X) != N):
		e = heappop(h) # e is (length, vertex) tuple
		T[last].append((e[1], e[0]))
		last = e[1]
		v = e[1]
		X.append(v)
		# when v added to X, the edge next to v need to change. 
		for edge in G[v]: # edge is (vertex, length)
			if edge[0] not in X and edge[0] != v:
				for i in range(0, len(h)):
					if h[i][1] == edge[0]:
						current = h[i][0]
						vw = edge[1]
						if vw < current:
							h[i] = (vw, edge[0])
							heapify(h)
	return dict(T)


G = {'A': [('B', 3), ('C',4)],
 'B': [('A', 3), ('C', 5),('D',6),('E',2)],
 'C': [('B', 5),('A',4),('E',7)],
 'D':[('B',6)],
 'E':[('B',2),('C',7)]}

print Question3(G)



