import sys
import collections
queue_size = []
max_states = []
flags = []
dominoes = []
with open(sys.argv[1], 'r') as f:
      contents = f.readlines()
      
queue_size = contents[1]
max_states = contents[2]
flags = contents[3]
dominoes = contents[4:]
#Breadth First Search
def bfs(dic, queue_size):
      visited, queue = set(), collections.deque([queue_size])
      visited.add(queue_size)
      while queue:
          vertex = queue.popleft()
          for neighbor in dominoes[vertex]:
                if neighbor not in dominoes[vertex]:
                        visited.add(neighbor)
                        queue.append(neighbor)
print(bfs(dic,queue_size))

#Iterative Deepening Search
def DLS(self,dominoes,target,max_states):
    if domiones == target: return True
    for i in self.graph[dominoes]:
          if(self.DLS(i,target,max_states-1)):
                  return False
    return False

def IDDFS(self,dominoes, target, max_states):
    for i in range(max_states):
        if(self.DLS(dominoes,target,i)):
            return True
    return False  

if g.IDDFS(dominoes, target, maxDepth) == True: 
    print ("Target is reachable from source " +
        "within max depth") 
else : 
    print ("Target is NOT reachable from source " +
        "within max depth")        