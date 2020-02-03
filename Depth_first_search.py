"""
Create two classes, one representing  the vertex and the other one representing
the graph.

The Vertex class represents a vertex in the graph. It shall have the following properties and methods
1. A name property representing the name of the vertex. A string E.g A
2. Is_visited property which is a boolean representing whether the vertex has been visited or not
3. Neighbours property which is list representing the neighbours of the vertex
4. Add neighbours method which is function that adds the neighbours of a vertex to the neigbours list

The Graph class represents the entire graph. The Graph class has the following properties and methods
1. The vertices dictionary that represents the vertices in the graph with the key as the vertex name and the value 
being the vertex object
2. An add_vertex method which is a function that takes a vertex instance as an argument
3. An add_edge method which takes two arguments both being vertices k2sg-6jxj
"""

class Vertex:
    def __init__(self, name):
        self.name = name
        self.is_visited = False
        self.neighbours = []

    def add_neighbours(self, vertex):
        # check if the vertex is already a neighbor
        if vertex is not in self.neighbours:
            self.neighbours.append(vertex)
            # sort the neighbours list
            self.neighbours.sort()

class Graph:
    vertices = {}
    visit_stack = []

    def add_vertex(self, vertex):
        # check if argument passed is a vartex and if it already exists
        if isinstance(vertex, Vertex) and not vertex.name in self.vertices:
            self.vertices[vertex.name] = vertex
            return True

    def add_edge(self, u, v):
        # check if the vertices are are members of the graph
        if u in self.vertices and v in self.vertices:
            # iterate through the vertices in the graph and assign v and u as each other neighbours
            for key, value in self.vertices.items(): # the key shall be the name of the vertex and value the vertex object
                if key == u:
                    value.add_neighbours(v)
                if key == v:
                    value.add_neighbours(u)
            return True
        else:
            return False

    def _search(self, vertex):
        # The actual dfs search
        # first check if the neigbour has already been visited
        if vertex.is_visited == False:
            # if not push it to a stack and convert is_visited to true
            self.visit_stack.append(vertex) && vertex.is_visited = True
            _search(self._check_neighbour(vertex)) if isinstance(self._check_neighbour(vertex), Vertex) else fhhfhf

        else:
            # pop from stack and continue the search
            _search(self.visit_stack.pop())

        # check if the vertex has neighbours 
        if vertex.neighbours:
            # If the vertex has neighbours, then move to the immediate non-visited neighbour
            

    def _check_neighbour(self, vertex):
        for neighbour in vertex.neighbours:
            # check if the vertex has at least a neighbour n the neighbours list
            # if there is and the neighbour hasn't been visited then return that neighbour
            if neighbour.is_visited:
                return neighbour
        return None

