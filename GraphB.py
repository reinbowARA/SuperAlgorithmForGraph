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

    # Эта функция удаляет ребро u-v из графика
    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)
 
    # Функция на основе DFS для подсчета достижимых вершин из v
    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)        
        return count
 
    # Функция для проверки того, можно ли рассматривать ребро u-v как следующее ребро в
    # Тур по Эйлеру
    def isValidNextEdge(self, u, v):
    # Ребро u-v допустимо в одном из следующих двух случаев:
  
          # 1) Если v - единственная смежная вершина u
        if len(self.graph[u]) == 1:
            return True
        else:
            '''
             2) Если существует несколько смежных, то u-v не является мостом
                Выполните следующие действия, чтобы проверить, является ли u-v мостом
  
            2.a) количество вершин, достижимых из u'''   
            visited =[False]*(self.V)
            count1 = self.DFSCount(u, visited)
 
            '''2.b) Удалите ребро (u, v) и после удаления ребра посчитайте
                вершины, достижимые из u'''
            self.rmvEdge(u, v)
            visited =[False]*(self.V)
            count2 = self.DFSCount(u, visited)
 
            #2.c) Добавьте ребро обратно к графику
            self.addEdge(u,v)
 
            # 2.d) Если количество больше, то ребро (u, v) является мостом
            return False if count1 > count2 else True
 
 
    # Печать Эйлерова тура
    def printEulerUtil(self, u):
        # Повторяется для всех вершин, смежных с этой вершиной
        for v in self.graph[u]:
            # Если ребро u-v не удалено и это допустимое следующее ребро
            if self.isValidNextEdge(u, v):
                print("%d-%d " %(u,v)),
                self.rmvEdge(u, v)
                self.printEulerUtil(v)
 
 
     
    ''' Основная функция, которая выводит эйлерову траекторию. Сначала он находит
        вершину нечетной степени (если таковая имеется), а затем вызывает printEulerUtil()
        чтобы напечатать путь '''
    def printEulerTour(self):
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) %2 != 0 :
                u = i
                break
        self.printEulerUtil(u)

    # Алгоритм Косайджу

    # Функция использует поиск в глубину
    def DFSUtil(self,v,visited):
            visited[v]= True
            print(v)
            for i in self.graph[v]:
                if visited[i]==False:
                    self.DFSUtil(i,visited)
    
    
    def fillOrder(self,v,visited, stack):           
            visited[v]= True
            for i in self.graph[v]:
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)
            stack = stack.append(v)
        
    
        # Функция, которая возвращает обратное (или транспонирование) этого графика
    def getTranspose(self):
            g = Graph(self.V)
    
            # Повторяется для всех вершин, смежных с этой вершиной
            for i in self.graph:
                for j in self.graph[i]:
                    g.addEdge(j,i)
            return g
 
  
  
    # Основная функция, которая находит и печатает все файлы
    # подключенные компоненты
    def printSCCs(self):
            
        stack = []
            # Отметьте все вершины как не посещенные (для первого DFS)
        visited =[False]*(self.V)
            # Заполните вершины в стеке в соответствии со временем их завершения
        for i in range(self.V):
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)
    
            # Создайте перевернутый график
        gr = self.getTranspose()
            # Отметить все вершины как не посещенные (для второго DFS)
        visited =[False]*(self.V)
            # Теперь обработайте все вершины в порядке, определенном стеком
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