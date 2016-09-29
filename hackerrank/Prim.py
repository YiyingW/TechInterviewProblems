'''
https://www.hackerrank.com/contests/master/challenges/primsmstsub?h_r=internal-search
'''
from heapq import heappush, heappop, heapify
import numpy as np

class Vertex(object):
	def __init__(self, name):
		self.name = name
		self.edges = []
	def add_edge(self, edge_to, length):
		self.edges.append((length, edge_to))

N, M = map(int, raw_input().split())

vertices = {}
for i in range(0, M): # read in edges line by line, edge by edge
	a, b, c = raw_input().split()
	length = int(c)
	if a not in vertices.keys():
		vertices[a] = Vertex(a)
		vertices[a].add_edge(b, length)
	else:
		vertices[a].add_edge(b, length)
	if b not in vertices.keys():
		vertices[b] = Vertex(b)
		vertices[b].add_edge(a, length)
	else:
		vertices[b].add_edge(a, length)


source = raw_input()

# initialize X = [s]
X = [source]
T = []
# initialize heap, heap has every element but source
h = []
source_edge_track = {}
for edge in vertices[source].edges:
	if edge[1] not in source_edge_track.keys():
		source_edge_track[edge[1]] = [edge[0]]
	else:
		source_edge_track[edge[1]].append(edge[0])
for i in source_edge_track.keys():
	heappush(h, (min(source_edge_track[i]), i))



for v in vertices.keys():
	if v != source and v not in source_edge_track.keys():
		heappush(h, (np.inf, v))
# finish initialize heap *_* # 


while (len(X) != N):

	e = heappop(h) # e is (length, node) tuple
	T.append(e)
	v = e[1]
	X.append(v)
	# when v added to X, the edge next to v need to change. 
	for edge in vertices[v].edges:
		if edge[1] not in X and edge[1] != v:
			for i in range(0, len(h)):
				if h[i][1] == edge[1]:
					current = h[i][0]

					vw = edge[0]
					if vw < current:
						h[i] = (vw, edge[1])
						heapify(h)

result = 0
#print T
for t in T:
	result += t[0]
print result


