from typing import Deque, List


class Task:
   def __init__(self, id: str, deps: List[str]):
       self.id = id
       self.deps = deps


"""
web:deploy ------------------------------
  |              |                     |
  v              |                     v
web:test          |                web-client:test
  |              |                     |
  v              |                     v
web:build <-------                 web-client:build
"""
allTasks = [
   Task(
       id="web:build",
       deps=[],
   ),
   Task(
       id="web:test",
       deps=["web:build"],
   ),
   Task(
       id="web:deploy",
       deps=["web:test", "web:build", "web-client:test"],
   ),
   Task(
       id="web-client:build",
       deps=[],
   ),
   Task(
       id="web-client:test",
       deps=["web-client:build"],
   ),
]


# Given a list of requested tasks to run, output a list of all necessary tasks
# to run, in a proper order.
# Input:
#   allTasks: a list of all task configurations
#   tasksToRun: ids of requested tasks to run
# Output: a list of task ids to run, in a proper order
# Requirements:
# - Must be correct
# - Must be performant on large graphs
# - Code should be easy to read
def getTasksToRun(allTasks: List[Task], tasksToRun: List[str]) -> List[str]:


   allNeeded: set = set()
   ans: list[str] = [] # returning ordered items
   allTaskSet = set(allTasks)
   q = Deque()


   def getTaskObjectbyId(id:str): # would build a dictionary later
       for task in allTasks:   
           # print(f'task.id: {task.id}')
           if task.id == id:
               return task


   for task in tasksToRun:
       # taskObject = getTaskObjectbyId(task)
       intermediateSteps =[]
       q.append(task)
       while(len(q) > 0 ):
               taskId = q.popleft()
               intermediateSteps.append(taskId)
               taskObj = getTaskObjectbyId(taskId)
               if(taskObj):
                   for dep in taskObj.deps:
                       q.append(dep)
      
       myVar = list(reversed(intermediateSteps))
       [ans.append(item) for item in myVar if item not in ans]




   return ans
   # getTaskObjectbyId()





print(getTasksToRun(allTasks, ["web:test"])) # ["web:build", "web:test"]
print(getTasksToRun(allTasks, ["web:test", "web:build"])) # ["web:build", "web:test"]
print(getTasksToRun(allTasks, ["web:deploy"])) # ["web:build", "web:test", "web-client:build", "web-client:test", "web:deploy"],or
# ["web-client:build", "web-client:test", "web:build", "web:test", "web:deploy"]
