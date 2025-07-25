# Shortest Distance Between Cities in a Network

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-2A78B6?style=for-the-badge&logo=networkx&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3175A2?style=for-the-badge&logo=matplotlib&logoColor=white)

-Samarth Mahesh

This project uses graphs to model a network of cities and applies Dijkstra's algorithm to find the shortest path between any two cities in the network.

## Objective

The goal is to create a five-city network where cities are nodes and the distances between them are weighted edges. After building this network graph, the program calculates and visualizes the shortest possible path from a user-selected starting city to a destination city.

---

## Example Network and Data

The network consists of five cities. The connections and distances are represented by the graph and adjacency matrix below.

**Graph Visualization:**

![Graph of the city network](https://github.com/user-attachments/assets/3e2d67dd-efb9-4976-91ae-c2c8de860999)


## Tools Used

*   **NetworkX**: The primary tool for creating, manipulating, and studying the structure of the city network. Cities are represented as nodes and the distances between them as weighted edges.
*   **Matplotlib**: Used for visualizing the graph. It draws the nodes, edges, and highlights the calculated shortest path, making the result easy to understand.
*   **Heapq**: A Python standard library module that provides an efficient implementation of a priority queue. This is used to optimize Dijkstra's algorithm by always selecting the next node with the minimum known distance.

---

**Adjacency Matrix:**
![Adjacency matrix showing distances between cities](https://github.com/user-attachments/assets/fd50b85a-f8b9-4de7-8cb3-c5d17519a38d)

---

## How It Works

The script performs the following steps:
1.  **Creates a Graph**: It uses `networkx` to build a weighted, undirected graph from a predefined dictionary of cities and distances.
2.  **Implements Dijkstra's Algorithm**: A custom implementation of Dijkstra's algorithm finds the shortest path from a start node to all other nodes in the graph. The use of a `heapq` priority queue makes this process efficient.
3.  **Visualizes the Result**: After calculating the path, `matplotlib` is used to draw the entire city network and then highlight the edges that form the shortest path in red.

---

## How to Run the Project

1.  The program will prompt you to enter the starting and destination cities by their index numbers.
2.  After you provide the input, it will print the shortest distance and the path, and then a Matplotlib window will open to show the visual representation of the graph and the highlighted path.

---
