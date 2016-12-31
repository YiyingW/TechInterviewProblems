"""
course schedule
"""
from collections import defaultdict

class Solution(object):
    

    visited = defaultdict(int)
    
    def to_adjacency_list(self, numCourses, edges):
        adjacency_dict = defaultdict(list)
        for i in range(0, numCourses):
            adjacency_dict[i] = []
        for edge in edges:
            adjacency_dict[edge[0]].append(edge[1])
        return adjacency_dict

    def DFS_visit(self, vertex, graph):
        
        if self.visited[vertex] == 1:
            return True
        self.visited[vertex] = -1 # it is in the searching state
        for v in graph[vertex]:
            if self.visited[v] == -1 or not self.DFS_visit(v, graph):
                return False 
        self.visited[vertex] = 1
        return True # no cycle


    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = self.to_adjacency_list(numCourses, prerequisites)
        for node in graph:
            #print self.visited

            if self.visited[node] != 1:
                if not self.DFS_visit(node, graph):
                    return False
        return True




c = Solution()

#print c.canFinish(4, [[0,1],[2,1],[0,2],[2,3]])

print c.canFinish(2, [[0,1],[1,0]])
