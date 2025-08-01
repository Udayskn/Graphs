class Solution:
    #O(V+E)
    def dfs(self,graph,node,visited,revOrder):
        if visited[node] != 0 :
            return True
        visited[node] = 1
        isCycle = False
        # order1.append(node)
        for nei in graph[node] :
            if visited[nei] == 0: #not visited
                isCycle = isCycle or self.dfs(graph,nei,visited,revOrder)
            elif visited[nei] == 1  : #Cycle
                return True
        revOrder.append(node)  #All successive (next) courses are visited
        visited[node] = 2   
        return isCycle
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for course in range(numCourses)]
        for prereq in prerequisites :
            graph[prereq[1]].append(prereq[0])
        # print(graph)
        isCycle = False
        visited = [0 for node in range(len(graph)) ]
        revOrder = []
        # print("test",visited)
        for node in range(len(graph)) :
            # print("test")
            if visited[node] == 0 :
                # print(node)
                isCycle = isCycle or self.dfs(graph,node,visited,revOrder)
        if isCycle :
            return []
        revOrder.reverse()
        return revOrder
        