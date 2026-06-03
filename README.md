# Intelligent Route Planner Using Graph Algorithms

## Overview

The Intelligent Route Planner is a Data Structures and Algorithms (DSA) project that finds the optimal route between locations using graph algorithms. The project models a city as a weighted graph where locations are represented as nodes and roads are represented as edges with distances as weights.

The system uses BFS, DFS, and Dijkstra's Algorithm to explore routes and compute the shortest path between a source and destination.

---

## Problem Statement

Modern navigation and logistics systems require efficient route planning to minimize travel time, fuel consumption, and operational costs. This project demonstrates how graph algorithms can be used to solve shortest-path problems in transportation networks.

---

## Features

* Graph Representation using Adjacency List
* Breadth First Search (BFS)
* Depth First Search (DFS)
* Dijkstra's Shortest Path Algorithm
* Priority Queue (Min Heap)
* Route Reconstruction
* Route Summary Generation
* Graph Visualization using NetworkX and Matplotlib
* Route Report Export

---

## Technologies Used

* Python
* NetworkX
* Matplotlib
* Heapq (Priority Queue)

---

## Project Structure

```text
Intelligent-Route-Planner-Graph-Algorithms/
│
├── data/
├── src/
├── outputs/
│   └── route_report.txt
│
├── images/
│   └── route_graph.png
│
├── docs/
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## DSA Concepts Used

### Graph Data Structure

The city road network is represented as a graph.

### Adjacency List

Stores neighboring locations and edge weights efficiently.

### BFS

Explores nodes level by level.

### DFS

Explores nodes depth first.

### Dijkstra Algorithm

Finds the shortest path between two locations in a weighted graph.

### Priority Queue

Used to efficiently select the next node with the minimum distance.

---

## Workflow

```text
Source & Destination
        ↓
Graph Creation
        ↓
Adjacency List
        ↓
BFS / DFS Traversal
        ↓
Dijkstra Algorithm
        ↓
Shortest Route
        ↓
Route Summary
        ↓
Graph Visualization
```

---

## Sample Graph

```text
A ----4---- B
|           |
2           5
|           |
C ----8---- D
 \         /
 10       2
   \     /
      E
      |
      3
      |
      F
```

---

## Sample Output

```text
BFS Traversal:
A B C D E F

DFS Traversal:
A B D C E F

Shortest Path:
A -> B -> D -> E -> F

Total Distance: 14
```

---

## Installation

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python main.py
```

---

## Output Files

### Route Report

```text
outputs/route_report.txt
```

### Graph Visualization

```text
images/route_graph.png
```

---

## Real-World Applications

* Google Maps
* Uber
* Ola
* Swiggy
* Zomato
* Logistics Optimization
* Delivery Route Planning
* Transportation Systems

---

## Learning Outcomes

* Understanding Graph Data Structures
* Implementing BFS and DFS
* Applying Dijkstra's Algorithm
* Using Priority Queues
* Path Reconstruction Techniques
* Graph Visualization
* Building Real-World DSA Projects

---

## Future Enhancements

* A* Search Algorithm
* Traffic-Based Route Planning
* Toll Cost Optimization
* Fuel Consumption Analysis
* Interactive GUI Dashboard
* Live Map Integration

---

## Author

Sinchana Gowda

A DSA-focused project demonstrating graph algorithms and route optimization techniques commonly used in navigation and logistics systems.
