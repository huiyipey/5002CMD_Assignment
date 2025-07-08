class Graph:
    def __init__(self):
        self.adj_list = dict()
        self.vertices = []
        # self.vertex_indices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            # self.vertex_indices[vertex] = len(self.vertices) - 1
            self.adj_list[vertex] = []  # Initialize with empty list

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            if from_vertex not in self.adj_list:
                self.adj_list[from_vertex] = []
            if to_vertex not in self.adj_list[from_vertex]:
                self.adj_list[from_vertex].append(to_vertex)

    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex in self.adj_list and to_vertex in self.adj_list[from_vertex]:
            self.adj_list[from_vertex].remove(to_vertex)

    def get_outgoing_adjacent(self, vertex):
        return self.adj_list.get(vertex, [])

    def get_incoming_adjacent(self, vertex):
        incoming = []
        for v in self.vertices:
            if v in self.adj_list and vertex in self.adj_list[v]:
                incoming.append(v)
        return incoming
