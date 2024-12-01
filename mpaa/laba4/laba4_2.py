import heapq
import random

def generate_random_graph(num_vertices, density=0.5, min_weight=1, max_weight=10):
    graph = {i: {} for i in range(num_vertices)}
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < density:
                weight = random.randint(min_weight, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

def dijkstra(G, start, end):
    # Инициализация расстояний и предшественников
    Distance = {vertex: float('infinity') for vertex in G}
    Parent = {vertex: None for vertex in G}
    Distance[start] = 0
    
    # Используем приоритетную очередь для извлечения вершины с минимальным расстоянием
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)
        
        # Если мы достигли конечной вершины
        if u == end:
            return build_path(Parent, start, end)
        
        # Если извлеченное расстояние больше текущего, пропускаем его
        if current_distance > Distance[u]:
            continue
        
        # Обновляем расстояния до смежных вершин
        for neighbor, weight in G[u].items():
            distance = current_distance + weight
            
            if distance < Distance[neighbor]:
                Distance[neighbor] = distance
                Parent[neighbor] = u
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Если конец не был достигнут, возвращаем признак отсутствия пути
    return "Путь не найден"

def build_path(Parent, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = Parent[current]
    path.reverse()
    
    if path[0] == start:
        return path
    else:
        return "Путь не найден"

# Пример использования
num_vertices = 10
density = 0.3
min_weight = 1
max_weight = 10

G = generate_random_graph(num_vertices, density, min_weight, max_weight)
start, end = 0, num_vertices - 1  # Начальная и конечная вершины

print("Сгенерированный граф:")
for vertex, edges in G.items():
    print(f"{vertex}: {edges}")

path = dijkstra(G, start, end)
print(f"Кратчайший путь из {start} в {end}: {path}")