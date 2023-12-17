from enum import Enum
from queue import PriorityQueue

input = open('aoc_17.txt', 'r')
lines = [line.strip() for line in input.readlines()]

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    
class Step():
    def __init__(self, cost: int, col: int, row: int, direction: Direction, steps: int):
        self.cost = cost
        self.col = col
        self.row = row
        self.direction = direction
        self.steps = steps
    def __lt__(self, other):
        if self.cost == other.cost:
            if self.col == other.col:
                if self.row == other.row:
                    if self.direction == other.direction:
                        return self.steps < other.steps
                    return self.direction.value < other.direction.value
                return self.row < other.row
            return self.col < other.col
        return self.cost < other.cost

def dijkstra(graph: list[list[int]], min_steps: int, max_steps: int):
    queue = PriorityQueue()
    queue.put(Step(0,0,0,Direction.RIGHT,1))
    queue.put(Step(0,0,0,Direction.DOWN,1))
    visited = set()
    
    while queue:
        curr: Step = queue.get()
        if (curr.col, curr.row, curr.direction, curr.steps) in visited:
            continue
        visited.add((curr.col, curr.row, curr.direction, curr.steps))
        
        new_col = curr.col + curr.direction.value[1]
        new_row = curr.row + curr.direction.value[0]
        
        if new_col < 0 or new_col >= len(graph[0]) or new_row < 0 or new_row >= len(graph):
            continue
        new_cost = curr.cost + graph[new_row][new_col]
        if min_steps <= curr.steps <= max_steps and new_col == len(graph[0]) - 1 and new_row == len(graph) - 1:
            return new_cost
        if curr.steps < min_steps:
            queue.put(Step(new_cost, new_col, new_row, curr.direction, curr.steps + 1))
            continue
        for new_direction in Direction:
            if new_direction.value[0] + curr.direction.value[0] == 0 and new_direction.value[1] + curr.direction.value[1] == 0:
                continue
            if new_direction == curr.direction:
                new_steps = curr.steps + 1
            else:
                new_steps = 1
            if new_steps > max_steps:
                continue
            queue.put(Step(new_cost, new_col, new_row, new_direction, new_steps))
    return -1

graph = [[int(item) for item in line] for line in lines]
print(dijkstra(graph, 4, 10))
    
