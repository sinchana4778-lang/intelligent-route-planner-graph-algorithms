import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):

        self.graph.setdefault(u, []).append((v, weight))
        self.graph.setdefault(v, []).append((u, weight))

    def bfs(self, start):

        visited = set()
        queue = [start]

        print("\nBFS Traversal:")

        while queue:

            node = queue.pop(0)

            if node not in visited:

                print(node, end=" ")

                visited.add(node)

                for neighbor, _ in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start):

        visited = set()

        print("\nDFS Traversal:")

        def helper(node):

            visited.add(node)

            print(node, end=" ")

            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    helper(neighbor)

        helper(start)

    def dijkstra(self, start, end):

        distances = {node: float('inf')
                     for node in self.graph}

        distances[start] = 0

        parent = {}

        pq = [(0, start)]

        while pq:

            current_distance, current_node = heapq.heappop(pq)

            for neighbor, weight in self.graph[current_node]:

                distance = current_distance + weight

                if distance < distances[neighbor]:

                    distances[neighbor] = distance

                    parent[neighbor] = current_node

                    heapq.heappush(
                        pq,
                        (distance, neighbor)
                    )

        path = []

        current = end

        while current != start:

            path.append(current)

            current = parent[current]

        path.append(start)

        path.reverse()

        return path, distances[end]

    def visualize(self):

        G = nx.Graph()

        for node in self.graph:

            for neighbor, weight in self.graph[node]:

                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)

        labels = nx.get_edge_attributes(
            G,
            'weight'
        )

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=2000
        )

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=labels
        )

        plt.title(
            "Intelligent Route Planner"
        )

        plt.savefig(
            "images/route_graph.png"
        )

        plt.show()


route_graph = Graph()

route_graph.add_edge("A", "B", 4)
route_graph.add_edge("A", "C", 2)
route_graph.add_edge("B", "D", 5)
route_graph.add_edge("C", "D", 8)
route_graph.add_edge("C", "E", 10)
route_graph.add_edge("D", "E", 2)
route_graph.add_edge("D", "F", 6)
route_graph.add_edge("E", "F", 3)

route_graph.bfs("A")
route_graph.dfs("A")

source = "A"
destination = "F"

path, distance = route_graph.dijkstra(
    source,
    destination
)

print("\n\nShortest Path:")
print(" -> ".join(path))

print("\nTotal Distance:", distance)

with open(
    "outputs/route_report.txt",
    "w"
) as file:

    file.write(
        f"Source: {source}\n"
    )

    file.write(
        f"Destination: {destination}\n"
    )

    file.write(
        f"Route: {' -> '.join(path)}\n"
    )

    file.write(
        f"Distance: {distance}"
    )

route_graph.visualize()