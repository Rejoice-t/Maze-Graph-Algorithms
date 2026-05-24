# Maze-Graph-Algorithms
## Project Overview

This project solves multiple graph problems using a maze represented as a text file. The maze is interpreted as a graph where each non-wall cell is treated as a vertex, and edges are created between neighboring cells.

The project implements:

- Breadth-First Search (BFS)
- Dijkstra’s Algorithm
- Prim’s Minimum Spanning Tree Algorithm

The project supports:

- 4-directional movement
- 8-directional movement

---

# Maze Format

Allowed symbols:

| Symbol | Meaning |
|---|---|
| S | Start cell |
| G | Goal cell |
| X | Wall |
| 0-9 | Open cell with numeric value |

Example:

```text
S1023
1XX24
230X5
2X111
3333G
```

---

# Algorithms Implemented

## Subtask A — Shortest Path

### Algorithm Used

- Breadth-First Search (BFS)

### Goal

Find the minimum number of moves from S to G.

---

## Subtask B — Minimum Cost Path

### Algorithm Used

- Dijkstra’s Algorithm

### Cost Model

- Entering Cost

### Formula

```text
cost(u,v) = value(v)
```

### Goal

Find the minimum total traversal cost from S to G.

---

## Subtask C — Movement Comparison

The project compares:

- 4-directional movement
- 8-directional movement

The comparison analyzes:

- shortest path length
- minimum traversal cost

---

## Subtask E — Minimum Spanning Tree

### Algorithm Used

- Prim’s Algorithm

### Goal

Construct a minimum spanning tree for the connected component containing S.

### Edge Weight Formula

```text
weight(u,v) = value(u) + value(v)
```

---

# How the Maze is Represented

The maze is stored as a 2D list.

Example:

```python
maze[row][col]
```

Each non-wall cell is treated as a graph vertex.

Vertices are represented using coordinates:

```text
(row, column)
```

---

# Graph Representation

The graph is represented implicitly using neighboring cells.

Edges are generated dynamically using movement rules:

- up
- down
- left
- right
- diagonal directions (for 8-directional movement)

Walls are excluded from the graph.

---

# Running the Program

## Command

```bash
python main.py maze_10x10_A.txt
```

---

# Files Included

| File | Purpose |
|---|---|
| main.py | Main program source code |
| maze_10x10_A.txt | Input maze |
| output.txt | Program results |
| README.md | Project instructions |
| report.pdf | Project report |

---

# Time and Space Complexity

## BFS

### Time Complexity

```text
O(V + E)
```

### Space Complexity

```text
O(V)
```

### Reason

BFS visits each vertex and edge at most once.

---

## Dijkstra’s Algorithm

### Time Complexity

```text
O((V + E) log V)
```

### Space Complexity

```text
O(V)
```

### Reason

A priority queue is used to efficiently retrieve the lowest-cost vertex.

---

## Prim’s Algorithm

### Time Complexity

```text
O(E log V)
```

### Space Complexity

```text
O(V)
```

### Reason

A priority queue is used to repeatedly select the minimum-weight edge.

---

# Discussion of Results

The project successfully demonstrated different graph algorithms on the maze graph.

Breadth-First Search produced the shortest path in terms of number of moves.

Dijkstra’s Algorithm produced the minimum-cost path using weighted traversal costs.

The shortest path and cheapest path were different because BFS minimizes moves while Dijkstra minimizes total cost.

Allowing diagonal movement reduced both the path length and traversal cost because additional edges created shorter routes through the graph.

Prim’s Algorithm successfully generated a minimum spanning tree connecting all reachable vertices while avoiding cycles.

---

# Output Summary

## Subtask A

### 4-Directional

- Minimum Moves: 18

### 8-Directional

- Minimum Moves: 11

---

## Subtask B

### 4-Directional

- Minimum Cost: 26

### 8-Directional

- Minimum Cost: 18

---

## Subtask E

- MST Total Weight: 390
- Vertices in Component: 76
- Edges in MST: 75
- Goal Reachable From Start: True
