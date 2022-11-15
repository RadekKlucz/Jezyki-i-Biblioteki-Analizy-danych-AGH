from collections import deque

class Graph:
    def __init__(self) -> None:
        self.graph = dict()
        

    def add_vertices(self, *args):
        """The function adds vertex to the graph.

        Args:
            *args (list): List of vertices.

        Raises:
            AssertionError: If vertex exists in graph, the function will return error.
        """
        for argument in args:
            try:
                if argument not in self.graph:
                    self.graph[argument] = list()
                else:
                    raise AssertionError
            except AssertionError:
                print(f"{argument} is vertex in the graph")


    def add_edges(self, *args):
        """The function adds edges to the graph.

        Args:
            *args (list): List of edges.

        Raises:
            AssertionError: If vertex exists in the graph, the function will raise error.
        """
        for argument in args:
            try:
                edge = list(argument)
                (point_1, point_2) = tuple(edge)
                if (point_1 in self.graph) and (point_2 not in self.graph[point_1]):
                    self.graph[point_1].append(point_2)
                elif point_1 not in self.graph:
                    self.graph[point_1] = list(point_2)
                else:
                    raise AssertionError
            except AssertionError:
                print(f"{argument} already exists in graph")


    def delete_vartex(self, vartex):
        """The function deletes the given vartex from the graph.

        Args:
            vartex (string): A vartex to delete.

        Raises:
            KeyError: If a vertex does not exist in the graph, the function will return KeyError.
        """
        try:
            if vartex in self.graph:
                for edges in self.graph[vartex]:
                    for values in self.graph[edges]:
                        if vartex == values:
                            self.graph[edges].remove(values)
                del self.graph[vartex]
            else:
                raise KeyError
        except KeyError:
            print(f"{vartex} is not vertex in the graph")


    def delete_edge(self, edge):
        """The function deletes a edge from the graph.

        Args:
            edge (string): A edge to delete

        Raises:
            KeyError: If a edge is not found in the graph, the function will raise KeyError.
        """
        try:
            for key in self.graph:
                for value in self.graph[key]:
                    string_of_edges = key + value
                    if edge == string_of_edges:
                        self.graph[key].remove(value)
                    else: 
                        raise KeyError            
        except KeyError:
            print(f"{edge} is not edge in the graph")


    def find_neighbors(self, vertex):
        """The function finds neighbors of a vertex. ????????????????????????????????????????????

        Args:
            vertex (string): A vertex to search for neighbors.
        
        Raises:
            KeyError: If the vertex is not found in the graph, the function will return KeyError.
        """
        try:
            if vertex in self.graph:
                return {i: self.graph[i] for i in self.graph[vertex]}
            else:
                raise KeyError
        except KeyError:
            print(f"{vertex} is not vertex in the graph")


    def bfs(self, vertex):
        """Breadth First Search function for a graph.

        Args:
            vertex (string): Start's vertex.
        
        Returns:
            output_iter (iter): Iterator of the vertices.
        
        Raises:
            KeyError: If a start's vertex does not exist in the graph, the function will return KeyError.

        """
        try:
            list_of_keys = list(i for i in self.graph.keys())
            if vertex in list_of_keys:
                position = list_of_keys.index(vertex)
                queue = deque()
                visited = len(self.graph) * [False]
                queue.append(vertex)
                visited[position] = True
                list_of_vartex = list()
                while len(queue) != 0:
                    vertex = queue.popleft()
                    list_of_vartex.append(vertex)
                    for i in self.graph[vertex]:
                        new_position = list_of_keys.index(i)
                        if visited[new_position] == False:
                            queue.append(i)
                            visited[new_position] = True
                return iter(list_of_vartex)
            else:
                raise KeyError
        except KeyError:
            print(f"{vertex} is not vertex in the graph")


    def dfs_secondary_function(self, vertex):
        """
        Secondary function for the main DFS.

        Args:
            vertex (_type_): Start's vertex
        
        Raises:
            KeyError: If vertex does not exist in the graph, the function will raise KeyError.

        """
        try:  
            if vertex in self.graph.keys():

                self.visited_dfs.add(vertex)
                self.list_of_vartex_dfs.append(vertex)
                for i in self.graph[vertex]:
                    if i not in self.visited_dfs:
                        self.dfs_secondary_function(i)
            else:
                raise KeyError
        except KeyError:
            print(f"{vertex} is not vertex in the graph")


    def dfs(self, vertex):
        """
        Depth First Search function for the graph.
        
        Args:
            vertex (string): Stars' vertex.
        
        Returns:
            output_iter (iter): Iterator of the vertices.
        """
        self.list_of_vartex_dfs= list()
        self.visited_dfs = set()
        self.dfs_secondary_function(vertex)
        return iter(self.list_of_vartex_dfs)


if __name__ == "__main__":
    a = Graph()
    # a.add_vertices("a", "b", "c", "d", "e")
    # a.add_edges("ab", "ab",  "ac", "bd", "cd", "de")
    a.add_vertices("0", "1", "2","3")
    a.add_edges("20","02", "01", "12", "23", "33")
    print(a.graph)
    # print(a.delete_vartex("g"))
    # a.delete_edge("ef")
    # print(a.find_neighbors("b"))
    # b = a.bfs("2")
    # print(b)
    # print(b.__next__())
    # print(b.__next__())
    c = a.dfs("2")
    print(c.__next__())
    print(c.__next__())
    print(c.__next__())
    print(c.__next__())
    
    

    