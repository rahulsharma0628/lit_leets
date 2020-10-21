class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        sortedOrder = []
        
        #initiate the graph
        inDegree = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        
        #build the graph
        for courses in prerequisites:
            inDegree[courses[0]] += 1
            graph[courses[1]].append(courses[0])
        
        #find sources
        sources = deque()
        for i in inDegree:
            if inDegree[i] == 0:
                sources.append(i)
                
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != numCourses:
            return False
        
        return True
        
        