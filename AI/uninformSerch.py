'''
In the circles of A to J, fill in numbers from 1 to 10 randomly such that the values in the triangles are equal to the summations of the values filled in the circles surrounding the triangles

    (a) Use Breadth First Search,
        Uniform Cost Search (deep level as cost),
        and Depth First Search to find out possible solution(s).

    (b) For these three methods also count the nodes expanded for finding the solution(s).
'''

import random

# 建立 NODE
graph = {
    "A": ["C","D","E"],
    "B": ["C","F"],
    "C": ["A","D","F"],
    "D": ["A","E","G"],
    "E": ["A","D","G"],
    "F": ["B","C","H","I"],
    "G": ["D","E","H","J"],
    "H": ["F","G","I","J"],
    "I": ["F","H"],
    "J": ["G","H"]
}


node_value = {
    "A" : random.randint(1,10),
    "B" : random.randint(1,10),
    "C" : random.randint(1,10),
    "D" : random.randint(1,10),
    "E" : random.randint(1,10),
    "F" : random.randint(1,10),
    "G" : random.randint(1,10),
    "H" : random.randint(1,10),
    "I" : random.randint(1,10),
    "J" : random.randint(1,10),

}

triangle = {
    "ACD" : node_value["A"]+node_value["C"]+node_value["D"],
    "ADE" : node_value["A"]+node_value["D"]+node_value["E"],
    "BCF" : node_value["B"]+node_value["C"]+node_value["F"],
    "DEG" : node_value["D"]+node_value["E"]+node_value["G"],
    "FHI" : node_value["F"]+node_value["H"]+node_value["I"],
    "HGJ" : node_value["H"]+node_value["G"]+node_value["J"]
}

triangle_value = {
    "ACD" : 19,
    "ADE" : 18,
    "BCF" : 11,
    "DEG" : 16,
    "FHI" : 17,
    "HGJ" : 22
}


# ---------------------------------------------------------
# Breadth First Search
# 從最開始的節點搜尋，用隊列

def BFS (graph,start):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)

    while (len(queue) > 0): # loop to visit each node
        vertex = queue.pop(0) # 拿出queue中的第一個元素並從隊列移除
        print(vertex, end=" ")
        
        nodes = graph[vertex]  # A的所有節點 C D E 存成nodes
        for neighbour in nodes:
            if neighbour not in visited: #如果還沒搜尋過
                queue.append(neighbour) #放進queue裡面
                visited.append(neighbour)


print("following is the Breadth First Search")
BFS(graph , "A")
print(end= "\n")
print(node_value)

# ---------------------------------------------------------

# Depth First Search
# 從最新的節點搜尋，用字典

def DFS (graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop() # 移除並取出陣列的最後一個值
        print(node, end=" ")
        if node not in visited:
            visited.add(node)

            if node == goal:
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

print("following is the  Depth First Search")
DFS(graph,"A","J")
print(end= "\n")
print(node_value)



# --------------------------------------------------------
from collections import defaultdict
from queue import PriorityQueue

# Unifom Cost Search  
class Graph:
    def __init__(self, directed): 
        """Parametrized constructor of class Graph 
        which takes True if Graph is directed otherwise it takes False"""
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        """Add Edges between two nodes along 
        with weight as Algorithm is of UCS"""
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        """It takes starting node and 
        goal node as parameters then it returns 
        a path using Uniform Cost Search Algorithm"""
        visited = []  
        queue = PriorityQueue()
        queue.put((0, current_node))
        
        while not queue.empty():
            item = queue.get()
            current_node =  item[1]
            
            if current_node == goal_node:
                print(current_node, end = " ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue
                    
                print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                        queue.put((neighbour[0], neighbour[1]))

g = Graph(False)
g.graph = defaultdict(list)
g.add_edge("A","C",1)
g.add_edge("A","D",1)
g.add_edge("A","E",2)
g.add_edge("B","C",1)
g.add_edge("C","D",2)
g.add_edge("D","E",1)
g.add_edge("B","F",2)
g.add_edge("C","F",3)
g.add_edge("D","G",2)
g.add_edge("E","G",1)
g.add_edge("F","H",2)
g.add_edge("G","H",1)
g.add_edge("H","I",2)
g.add_edge("H","J",3)
g.add_edge("F","I",2)
g.add_edge("G","J",3)

print("following is the UCS")
g.ucs("A","J")
print(end= "\n")
print(node_value)