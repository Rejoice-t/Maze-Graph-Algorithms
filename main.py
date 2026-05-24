
# Maze Graph Project - Subtask A
# Student Name:Rejoice Teca
# Student ID:
# Language: Python

from collections import deque
import sys
import heapq


# Read maze from file
def read_maze(filename):

    maze = []

    with open(filename, 'r') as file:

        for line in file:
            maze.append(list(line.strip()))

    return maze


# Find Start (S)
def find_start(maze):

    for row in range(len(maze)):
        for col in range(len(maze[0])):

            if maze[row][col] == 'S':
                return (row, col)

    return None


# Find Goal (G)
def find_goal(maze):

    for row in range(len(maze)):
        for col in range(len(maze[0])):

            if maze[row][col] == 'G':
                return (row, col)

    return None


# Check if cell is valid

def is_valid(maze, row, col):

    rows = len(maze)
    cols = len(maze[0])

    return (
        0 <= row < rows and
        0 <= col < cols and
        maze[row][col] != 'X'
    )

# Get numeric value of a cell
# S and G have value 0
def get_value(cell):

    if cell == 'S' or cell == 'G':
        return 0

    return int(cell)


# Get neighboring cells
# movement = 4 or 8
def get_neighbors(maze, row, col, movement=4):

    directions4 = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    directions8 = directions4 + [
        (-1, -1), # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1)    # down-right
    ]

    directions = directions4 if movement == 4 else directions8

    neighbors = []

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if is_valid(maze, new_row, new_col):
            neighbors.append((new_row, new_col))

    return neighbors


# Reconstruct path
def reconstruct_path(parent, start, goal):

    path = []

    current = goal

    while current != start:

        path.append(current)
        current = parent[current]

    path.append(start)

    path.reverse()

    return path


# Breadth-First Search (BFS)
def bfs_shortest_path(maze, movement=4):

    start = find_start(maze)
    goal = find_goal(maze)

    # Queue for BFS
    queue = deque()

    # Add start node
    queue.append(start)

    # Track visited nodes
    visited = set()

    visited.add(start)

    parent = {}

    # Distance from start
    distance = {}

    distance[start] = 0

    while queue:

        current = queue.popleft()

        # Stop if we reach goal
        if current == goal:
            break

        row, col = current

        # Explore neighbors
        for neighbor in get_neighbors(maze, row, col, movement):

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)

                parent[neighbor] = current

                distance[neighbor] = distance[current] + 1

    # Check if goal reachable
    if goal not in visited:
        return None

    path = reconstruct_path(parent, start, goal)

    return {
        "moves": distance[goal],
        "path": path
    }

# Dijkstra's Algorithm
# Minimum Cost Path
def dijkstra_min_cost(maze, movement=4):

    start = find_start(maze)
    goal = find_goal(maze)

    # Priority Queue
    # (cost, current_node)
    pq = []

    heapq.heappush(pq, (0, start))

    # Distance dictionary
    dist = {}

    dist[start] = 0

    # Parent dictionary
    parent = {}

    # Visited nodes
    visited = set()

    while pq:

        current_cost, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        # Stop if goal reached
        if current == goal:
            break

        row, col = current

        # Explore neighbors
        for neighbor in get_neighbors(maze, row, col, movement):

            nr, nc = neighbor

            # Cost of entering neighbor
            move_cost = get_value(maze[nr][nc])

            new_cost = current_cost + move_cost

            # Relaxation step
            if neighbor not in dist or new_cost < dist[neighbor]:

                dist[neighbor] = new_cost

                parent[neighbor] = current

                heapq.heappush(
                    pq,
                    (new_cost, neighbor)
                )

    # Goal unreachable
    if goal not in dist:
        return None

    path = reconstruct_path(parent, start, goal)

    return {
        "cost": dist[goal],
        "path": path
    }

# Prim's Algorithm
# Minimum Spanning Tree
def prim_mst(maze, movement=4):

    start = find_start(maze)
    goal = find_goal(maze)

    # Priority Queue
    # (weight, current_node, parent)
    pq = []

    heapq.heappush(pq, (0, start, None))

    # Visited vertices
    visited = set()

    # MST edges
    mst_edges = []

    # Total MST weight
    total_weight = 0

    while pq:

        weight, current, parent = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        # Add edge to MST
        if parent is not None:

            mst_edges.append(
                (parent, current, weight)
            )

            total_weight += weight

        row, col = current

        # Explore neighbors
        for neighbor in get_neighbors(
            maze,
            row,
            col,
            movement
        ):

            if neighbor not in visited:

                nr, nc = neighbor

                current_value = get_value(
                    maze[row][col]
                )

                neighbor_value = get_value(
                    maze[nr][nc]
                )

                edge_weight = (
                    current_value +
                    neighbor_value
                )

                heapq.heappush(
                    pq,
                    (
                        edge_weight,
                        neighbor,
                        current
                    )
                )

    goal_reachable = goal in visited

    return {
        "total_weight": total_weight,
        "vertex_count": len(visited),
        "edge_count": len(mst_edges),
        "edges": mst_edges,
        "goal_reachable": goal_reachable
    }

# Print MST Results
def print_mst_results(result, movement):

    print("========== SUBTASK E ==========")
    print(f"Movement Mode: {movement}-directional")
    print()

    print(f"MST Total Weight: {result['total_weight']}")
    print(f"Vertices in Component: {result['vertex_count']}")
    print(f"Edges in MST: {result['edge_count']}")
    print(f"G Reachable From S: {result['goal_reachable']}")

    print()
    print("MST Edges:")

    for parent, child, weight in result['edges']:

        print(
            f"{parent} -> {child} : weight = {weight}"
        )

# Print results
def print_results(result, movement):

    print("========== SUBTASK A ==========")
    print(f"Movement Mode: {movement}-directional")
    print()

    if result is None:
        print("No path found.")
        return

    print(f"Minimum Moves: {result['moves']}")
    print()

    print("Path:")

    path_string = " -> ".join(map(str, result['path']))

    print(path_string)

# Print Dijkstra results
def print_dijkstra_results(result, movement):

    print("========== SUBTASK B ==========")
    print(f"Movement Mode: {movement}-directional")
    print("Cost Model: Entering Cost")
    print()

    if result is None:
        print("No path found.")
        return

    print(f"Minimum Cost: {result['cost']}")
    print()

    print("Path:")

    path_string = " -> ".join(map(str, result['path']))

    print(path_string)

# Main Program
def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py maze.txt")
        return

    filename = sys.argv[1]

    maze = read_maze(filename)

    # 4-directional movement
    movement_mode = 4

    bfs_result_4 = bfs_shortest_path(
        maze,
        movement=movement_mode
    )

    dijkstra_result_4 = dijkstra_min_cost(
        maze,
        movement=movement_mode
    )

    print_results(
        bfs_result_4,
        movement=movement_mode
    )

    print()

    print_dijkstra_results(
        dijkstra_result_4,
        movement=movement_mode
    )

    print("\n")

    # 8-directional movement
    movement_mode = 8

    bfs_result_8 = bfs_shortest_path(
        maze,
        movement=movement_mode
    )

    dijkstra_result_8 = dijkstra_min_cost(
        maze,
        movement=movement_mode
    )

    print_results(
        bfs_result_8,
        movement=movement_mode
    )

    print()

    print_dijkstra_results(
        dijkstra_result_8,
        movement=movement_mode
    )

    print("\n")

    print("\n")

    # Subtask E - MST
    mst_result = prim_mst(
        maze,
        movement=4
    )

    print_mst_results(
        mst_result,
        movement=4
    )

    # Subtask C Comparison
    print("========== SUBTASK C ==========")

    print("\nShortest Path Comparison")
    print(f"4-directional moves: {bfs_result_4['moves']}")
    print(f"8-directional moves: {bfs_result_8['moves']}")

    print()

    print("Minimum Cost Comparison")
    print(f"4-directional cost: {dijkstra_result_4['cost']}")
    print(f"8-directional cost: {dijkstra_result_8['cost']}")
if __name__ == "__main__":
    main()  