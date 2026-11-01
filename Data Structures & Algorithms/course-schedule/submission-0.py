class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            reqMap[course].append(prereq)
        
        visited = set()

        def dfs(courses):
            if courses in visited:
                return False

            if reqMap[courses] == []:
                return True
            
            visited.add(courses)
            for c in reqMap[courses]:
                if not dfs(c):
                    return False
            
            visited.remove(courses)
            reqMap[courses] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True