import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Добавление ребра в граф
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Найти подмножество, к которому принадлежит элемент i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Объединить два подмножества x и y
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # Прикрепить меньшую по рангу структуру к корню более высокой по рангу структуры
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Основной алгоритм Крускала
    def kruskal_mst(self):
        result = []  # Это будет содержать результат MST

        # Шаг 1: Сортировка всех ребер в порядке возрастания их веса
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Создание V подмножеств с единственным элементом
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Количество ребер в MST будет V-1
        e = 0  # Инициализация счетчика ребер
        i = 0  # Инициализация счетчика отсортированных ребер

        # Пока не добавлено V-1 ребер
        while e < self.V - 1:

            # Шаг 2: Выбрать ребро с наименьшим весом
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # Если включение этого ребра не образует цикл
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Напечатать содержимое MST
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
        return result

def generate_random_graph(vertices, edge_probability=0.5, max_weight=10):
    graph = Graph(vertices)
    edges = set()
    for u in range(vertices):
        for v in range(u + 1, vertices):
            if random.random() < edge_probability:
                weight = random.randint(1, max_weight)
                graph.add_edge(u, v, weight)
                edges.add((u, v, weight))
    # Ensure the graph is connected by adding a spanning tree
    for u in range(1, vertices):
        v = random.randint(0, u - 1)
        weight = random.randint(1, max_weight)
        graph.add_edge(u, v, weight)
        edges.add((u, v, weight))
    return graph, edges

# Пример использования
random.seed(100)  # Для повторяемости результатов
vertices = 6
g, edges = generate_random_graph(vertices)

# Вывод сгенерированного графа
print("Generated Graph:")
for u, v, weight in edges:
    print(f"{u} -- {v} == {weight}")

# Построение минимального остовного дерева
mst = g.kruskal_mst()