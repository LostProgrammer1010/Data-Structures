from __future__ import annotations

class Node:

    def __init__(self, val: int = 0):
        self.val = val
        self.neighbors = []

    def add_neighbor(self, node: Node):
        if node not in self.neighbors:
            self.neighbors.append(node)
            node.neighbors.append(self)
        else: print("Node is already a neighbor")

    def remove_neighbor(self, node: Node):
        if node in self.neighbors:
            self.neighbors.remove(node)
            node.neighbors.remove(self)
        else: print("Node is not a neighbor")

    def __str__(self):
        return (f"{self.val}           {[neighbor.val for neighbor in self.neighbors]}")
    

class Graph:
    def __init__(self, nodes: list[Node] = []):
        self.nodes = nodes
        # Prevents a node from being adding with neighbors that do not exist in the graph
        for node in self.nodes:
            for neighbors in node.neighbors:
                if neighbors not in self.nodes:
                    self.remove(neighbors)

    def add_node(self, node: Node):
        if node not in self.nodes: self.nodes.append(node)
        else: print("Node is already apart of the graph")

    def remove_node(self, node: Node):
        if node in self.nodes:
            for neighbor in node.neighbors:
                neighbor.remove_neighbor(node)
            self.nodes.remove(node)
        else: print("Node is not in the graphr")

    def __str__(self):
        graph_string = "Value        Neighbors\n----------------------\n"
        for node in self.nodes:
            graph_string = graph_string + node.__str__() + "\n"
        return graph_string

if __name__ == "__main__":

    graph_nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]

    for node in graph_nodes:
        graph_nodes[0].add_neighbor(node)

    for i in range(3,len(graph_nodes)):
        graph_nodes[2].add_neighbor(graph_nodes[i]) 



    graph = Graph(graph_nodes)

    print(graph)













