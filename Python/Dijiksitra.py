import heapq
class Solution:
    #Dijiksitra  T.C = O((E+V)logV)
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        effort = [ [1e6 for col in range(len(row))] for row in heights ]         #O(V)
        effort[0][0] = 0
        pq = [[(0,0),0]] # list of node and distance(for priority ordering)
        while pq :
            # print(pq[0])
            node, nodeEffort = heapq.heappop(pq)                               #O(VlogV)
            # print(node,nodeEffort)
            noder, nodec = node
            if nodeEffort > effort[noder][nodec] : #unimp edge i.e node effot is updated inbw
                continue
            for neir in noder+1, noder-1 : #vertical neighbors
                neic = nodec
                if neir not in range(len(heights)) : #invalid node
                    continue
                newEffort = max(nodeEffort , abs(heights[noder][nodec] - heights[neir][neic]))
                
                if newEffort < effort[neir][neic] :
                    effort[neir][neic] = newEffort
                    heapq.heappush(pq,[(neir,neic),newEffort])                  #O(ElogE)
            for neic in nodec+1, nodec-1 : #horizontal neighbors
                neir = noder
                if neic not in range(len(heights[neir])) : #invalid node
                    continue
                newEffort = max(nodeEffort , abs(heights[noder][nodec] - heights[neir][neic]))
                # print(node,neir,newEffort,effort[neir][neic])
                if newEffort < effort[neir][neic] :
                    effort[neir][neic] = newEffort
                    heapq.heappush(pq,[(neir,neic),newEffort])
            # print(pq)
        # print(effort)
        return effort[len(heights)-1][len(heights[0])-1]