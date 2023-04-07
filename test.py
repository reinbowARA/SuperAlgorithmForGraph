from GraphB import Graph
from GraphB import EilerGraph

graph = Graph(6, directed=True)
graph.addEdge(1, 6)
graph.addEdge(1, 3)
graph.addEdge(2, 1)
graph.addEdge(2, 5)
graph.addEdge(3, 4)
graph.addEdge(5, 1)
graph.addEdge(5, 6)
graph.addEdge(5, 6)
graph.addEdge(6, 3)
graph.addEdge(6, 4)
print("Алгоритм Тарьяна:")
graph.topologicalSort() 

 
graph = Graph (5)
graph.addEdge(1, 0)
graph.addEdge(0, 2)
graph.addEdge(2, 1)
graph.addEdge(0, 3)
graph.addEdge(3, 4)
graph.addEdge(3, 2)
graph.addEdge(3, 1)
graph.addEdge(2, 4)
print("\nАлгоритм Флёри:")
graph.printEulerTour()

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4) 
print ("\nАлгоритм Косайджу")
g.printSCCs()

gr = EilerGraph
print("Алгоритм нахождения эйлеровых циклов: \nвведите количество вершин и ребер через пробел, потом вводите сами ребра через пробел и переносом через enter")
#gr.PrintEilerNode()


