from collections import defaultdict
import queue

class Graph:

    def __init__(self, vertices, directed=False):
        self.graph = defaultdict(list)
        self.V = vertices 
        self.directed = directed


    def addEdge(self, frm, to):
        self.graph[frm].append(to)
        if self.directed is False:
            self.graph[to].append(frm)
        else:
            self.graph[to] = self.graph[to]

    # алгоритм Тарьяна
    def visitNode(self, s, visited, sortlist):
        visited[s] = True
        for i in self.graph[s]:
            if not visited[i]:
                self.visitNode(i, visited, sortlist)
        sortlist.insert(0, s)

    def topologicalSort(self):
        visited = {i: False for i in self.graph}
        sortlist = []

        for v in self.graph:
            if not visited[v]:
                self.visitNode(v, visited, sortlist)
        print(sortlist)

    # алгоритм Флёри

    # This function removes edge u-v from graph   
    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)
 
    # A DFS based function to count reachable vertices from v
    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)        
        return count
 
    # The function to check if edge u-v can be considered as next edge in
    # Euler Tour
    def isValidNextEdge(self, u, v):
        # The edge u-v is valid in one of the following two cases:
  
          #  1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
            return True
        else:
            '''
             2) If there are multiple adjacents, then u-v is not a bridge
                 Do following steps to check if u-v is a bridge
  
            2.a) count of vertices reachable from u'''   
            visited =[False]*(self.V)
            count1 = self.DFSCount(u, visited)
 
            '''2.b) Remove edge (u, v) and after removing the edge, count
                vertices reachable from u'''
            self.rmvEdge(u, v)
            visited =[False]*(self.V)
            count2 = self.DFSCount(u, visited)
 
            #2.c) Add the edge back to the graph
            self.addEdge(u,v)
 
            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            return False if count1 > count2 else True
 
 
    # Print Euler tour starting from vertex u
    def printEulerUtil(self, u):
        #Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            #If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v):
                print("%d-%d " %(u,v)),
                self.rmvEdge(u, v)
                self.printEulerUtil(v)
 
 
     
    '''The main function that print Eulerian Trail. It first finds an odd
   degree vertex (if there is any) and then calls printEulerUtil()
   to print the path '''
    def printEulerTour(self):
        #Find a vertex with odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) %2 != 0 :
                u = i
                break
        # Print tour starting from odd vertex
        self.printEulerUtil(u)

    # Алгоритм Косайджу
    # A function used by DFS
    def DFSUtil(self,v,visited):
            # Mark the current node as visited and print it
            visited[v]= True
            print(v)
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[v]:
                if visited[i]==False:
                    self.DFSUtil(i,visited)
    
    
    def fillOrder(self,v,visited, stack):
            # Mark the current node as visited
            visited[v]= True
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[v]:
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)
            stack = stack.append(v)
        
    
        # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
            g = Graph(self.V)
    
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph:
                for j in self.graph[i]:
                    g.addEdge(j,i)
            return g
 
  
  
    # The main function that finds and prints all strongly
    # connected components
    def printSCCs(self):
            
        stack = []
            # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
            # Fill vertices in stack according to their finishing
            # times
        for i in range(self.V):
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)
    
            # Create a reversed graph
        gr = self.getTranspose()
            
            # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)
    
            # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited)
                print("")

class EilerGraph:

    def PrintEilerNode():
        E, v = EilerGraph.input_data()
        if not EilerGraph.check_v_for_parity(int(v), E):
            print('NONE')
            return
        paths = []
        while sum([1 for link in E if not link.used]) > 0:
            current_top = EilerGraph.search_not_used_link(E)
            current_path = [current_top, ]
            paths.append(EilerGraph.fill_path(current_path, current_top, E))
        while len(paths)>1:
            paths = EilerGraph.merge_paths(paths)
        print(" ".join(paths[0]))


    def merge_paths(paths):
        for i in range(len(paths)):
            for j in range(len(paths)):
                same_top = EilerGraph.get_same_top(paths[i], paths[j])
                if i != j and same_top:
                    i = paths[i]
                    j = paths[j]
                    jj = [j[(j.index(same_top)+1+k)%len(j)] for k in range(len(j)-1)]
                    ii = i[:(i.index(same_top)+1)] + jj + i[(i.index(same_top)):]
                    paths.remove(j)
                    paths.remove(i)
                    paths.append(ii)
                    return paths


    def get_same_top(path1, path2):
        for i in path1:
            for j in path2:
                if i == j:
                    return i
        return None


    def fill_path(current_path, current_top, E):
        for link in E:
            if current_top in link.e and not link.used:
                link.used = True
                current_top = link.get_another_top_from_link(current_top)
                if current_path[0] == current_top:
                    return current_path
                current_path.append(current_top)
        return EilerGraph.fill_path(current_path, current_top, E)


    def check_v_for_parity(count_v, E):
        dict_v = {}
        for i in range(1, count_v+1):
            dict_v[i] = sum([1 for link in E if str(i) in link.e])
            if dict_v[i] % 2 == 1 or dict_v[i] == 0:
                return False
        return True


    def search_not_used_link(E):
        for link in E:
            if not link.used:
                return link.e[0]
        return None


    def input_data():
        v, e = input().split()
        E = []
        for i in range(int(e)):
            E.append(EilerGraph.Link(input().split()))
        return E, v

    class Link:
        def __init__(self, e):
            self.e = e
            self.used = False

        def get_another_top_from_link(self, top):
            return self.e[self.e.index(top)-1]