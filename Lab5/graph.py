from collections import deque


class Graph:
    def __init__(self) -> None:
        self.graph = dict()

    
    def __str__(self) -> str:
        return f"You have created the graph which that looks like this: {self.graph}"
        

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
                print(f"{argument} is vertex in the graph")  # zamienił stryjek siekierkę na kijek


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
                point_1, point_2 = edge
                if (point_1 in self.graph and point_2 in self.graph) and (point_2 not in self.graph[point_1]):
                    self.graph[point_1].append(point_2)
                else:
                    raise AssertionError
            except (AssertionError, ValueError):
                if ValueError:  # ten warunek jest zawsze prawdziwy
                    print(f"{argument} is not correct edge.")
                elif (point_1 or point_2) not in self.graph:
                    print(f"{point_1} or {point_2} is not a vertex in the graph.")
                else:
                    print(f"{argument} already exists in graph.")


    def delete_vertex(self, input_vartex):
        """The function deletes the given vartex from the graph.

        Args:
            vartex (string): A vartex to delete.

        Raises:
            KeyError: If a vertex does not exist in the graph, the function will return KeyError.
        """
        if input_vartex in self.graph:
            # find edges that contain input vertex that
            for vertex in self.graph:
                if edge in self.graph[vertex]:
                    self.graph[vertex].remove(edge)
            del self.graph[input_vartex]
        else:
            print(f"{input_vartex} is not vertex in the graph")
            


    def delete_edge(self, edge):
        """The function deletes a edge from the graph.

        Args:
            edge (string): A edge to delete

        Raises:
            KeyError: If a edge is not found in the graph, the function will raise KeyError.
        """
        try:
            (point_1, point_2) = edge
            if point_1 in self.graph and point_2 in self.graph:
                for key in self.graph:
                    for value in self.graph[key]:
                        string_of_edges = str(key) + str(value)  # to nie może być robione na stringach
                        if edge == string_of_edges:
                            self.graph[key].remove(value)
            else:
                raise KeyError            
        except KeyError:
            print(f"{edge} is not edge in the graph.")


    def find_neighbors(self, vertex):
        """The function finds neighbors of a vertex.

        Args:
            vertex (string): A vertex to search for neighbors.

        Returns:
            (dict) dictionary with the neighbors and edges of the vertex.
        
        Raises:
            KeyError: If the vertex is not found in the graph, the function will return KeyError.
        """
        try:
            if vertex in self.graph:
                return {i: self.graph[i] for i in self.graph[vertex]}
            else:
                raise KeyError
        except KeyError:
            print(f"{vertex} is not vertex in the graph.")


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
            print(f"{vertex} is not vertex in the graph.")


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
            return print(f"{vertex} is not vertex in the graph")


    def dfs(self, vertex):
        """
        Depth First Search function for the graph.
        
        Args:
            vertex (string): Stars' vertex.
        
        Returns:
            output_iter (iter): Iterator of the vertices.
        """
        self.list_of_vartex_dfs= list()
        self.visited_dfs = set()  # to nie powinien być atrybut
        self.dfs_secondary_function(vertex)
        return iter(self.list_of_vartex_dfs)

def main():
    """
    The main function that runs the program.
    """
    # Create the vertices
    print("Put list of vertices: ")
    vertices = input(">>")
    vertices = vertices.split()
    graph = Graph()
    print(vertices)
    graph.add_vertices(*vertices)
    # Create the edges
    print("Put edges: ")
    edges = input(">>")
    edges = edges.split()
    graph.add_edges(*edges)
    # Choose a action
    print("What do you want to do?")
    action = input(">>")
    action = action.lower()
    match action:
        case ("delete vertex" | "dv"):
            print("Input vertex to delete: ")
            vertex = input(">>")
            graph.delete_vertex(vertex)
        case ("delete edge" | "de"):
            print("Input edge to delete: ")
            edge = input(">>")
            graph.delete_edge(edge)
        case ("find neighbors" | "fn"):
            print("Input vertex to find neighbors: ")
            vertex = input(">>")
            print(graph.find_neighbors(vertex))
        case "bfs":
            print("Input vertex to bfs: ")
            vertex = input(">>")
            bfs = graph.bfs(vertex)
            print("How many times do you want iterate?")
            number = int(input(">>"))
            try:
                for i in range(number):
                    print(bfs.__next__())
            except StopIteration:
                print("End iteration.")
        case "dfs":
            print("Input vertex to dfs: ")
            vertex = input(">>")
            dfs = graph.dfs(vertex)
            print("How many times do you want iterate?")
            number = int(input(">>"))
            try:
                for i in range(number):
                    print(dfs.__next__())
            except StopIteration:
                print("End iteration.")

        case ("nothing" | "n"):
            print("Good bye.")
        case _:
            print("Invalid input.")
    print(graph.__str__())


if __name__ == "__main__":
        main()

    # graph = Graph()
    # graph.add_vertices("0", "1", "2", "3")
    # graph.add_edges("20","02", "01", "12", "23", "33")
    # print(graph.__str__())
    # # graph.delete_vartex("2")
    # # graph.delete_edge("02")
    # print(graph.find_neighbors("3"))

    # bfs = graph.bfs("2")
    # print(bfs.__next__())
    # print(bfs.__next__())
    # dfs = graph.dfs("2")
    # print(graph.__next__())
    # print(graph.__next__())