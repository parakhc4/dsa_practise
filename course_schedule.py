class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node,safe):
            if safe[node] == 2:
                return True
            elif safe[node] == 1:
                return False
            
            safe[node] = 1
            for nd in adj_list[node]:
                if dfs(nd,safe) == False:
                    return False
            
            safe[node] = 2
            return True         
            
        adj_list = defaultdict(set)
        for precourse, targetcourse in prerequisites:
            adj_list[targetcourse].add(precourse)

        safe = [0] * numCourses

        for i in range(numCourses):
            if safe[i] == 2:
                pass
            else:
                if dfs(i,safe) == False:
                    return False
        return True