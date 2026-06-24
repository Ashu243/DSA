from collections import deque
numCourses = 2
prerequisites = [[1,0],[0,1]]

def course_schedule(prerequisites, numCourses):
    adj_list = [[] for _ in range(numCourses)]

    indegrees = [0]*numCourses

    for u,v in prerequisites:
        adj_list[v].append(u)
        indegrees[u] += 1
    
    queue = deque([])

    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbour in adj_list[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)

    if len(result) == numCourses:
        return True
    return False
    
print(course_schedule(prerequisites, numCourses))



# def course_scheduleII(prerequisites, numCourses):
#     adj_list = [[] for _ in range(numCourses)]

#     indegrees = [0]*numCourses

#     for u,v in prerequisites:
#         adj_list[v].append(u)
#         indegrees[u] += 1
    
#     queue = deque([])

#     for i in range(numCourses):
#         if indegrees[i] == 0:
#             queue.append(i)

#     result = []

#     while queue:
#         node = queue.popleft()
#         result.append(node)

#         for neighbour in adj_list[node]:
#             indegrees[neighbour] -= 1
#             if indegrees[neighbour] == 0:
#                 queue.append(neighbour)

#     if len(result) == numCourses:
#         return result
#     return []


