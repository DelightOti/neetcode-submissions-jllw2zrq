class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # make the premap

        preMap = {}

        for course in range(numCourses):
            preMap[course] = []
        
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visiting = set()
        visited = set()
        res = []
        # iterate over the courses tracking what u visited

        def cycle(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True

            visiting.add(course)

            for pre in preMap[course]:
                if cycle(pre) == False:
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)

        for course in range(numCourses):
            if cycle(course) == False:
                return []
        return res