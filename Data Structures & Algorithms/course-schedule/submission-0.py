class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(src, adj, visit, path, topSort):
            if src in path: 
                return False
            if src in visit: 
                return True
            visit.add(src)
            path.add(src)

            for neighbour in adj[src]:
                if not dfs(neighbour, adj, visit, path, topSort):
                    return False
            path.remove(src)
            topSort.append(src)
            return True

        adjacency = {}
        for i in range(numCourses):
            adjacency[i] = []
        for course, prereq in prerequisites: 
            adjacency[course].append(prereq)
        
        topSort = []
        visit = set()
        path = set()
        for i in range(numCourses):
            if dfs(i, adjacency, visit, path, topSort) == False:
                return False

        return True