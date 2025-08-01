import heapq
class Solution:
    def manhD(self,P1,P2) :
        return abs(P1[0] - P2[0]) + abs(P1[1] - P2[1])
    #PRIMS Algo T.C = O((E+V)logV)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = [[0,0]] #edge dist and pointIndex
        visited = [False]*len(points)         #  O(V)
        minCost = 0
        while minheap :
            curD, pointIndex = heapq.heappop(minheap)  #O(VlogV)
            # print(point)
            if visited[pointIndex]:
                continue
            minCost += curD
            visited[pointIndex] = True
            point = points[pointIndex]
            for neiIndex,neiPoint in enumerate(points): #O(ElogV)
                if visited[neiIndex]:
                    continue
                heapq.heappush(minheap,[self.manhD(point,neiPoint),neiIndex])
        return minCost