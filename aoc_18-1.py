from dataclasses import dataclass
from enum import Enum

input = open('aoc_18.txt', 'r')
lines = [line.strip() for line in input.readlines()]

@dataclass(frozen=True)
class Point:
    row: int
    col: int
    def __add__(self, other):
        return Point(row=self.row + other.row, col=self.col + other.col)
    def __mul__(self, other):
        return Point(row=self.row * other, col=self.col * other)

class Direction(Enum):
    U = Point(row=-1, col=0)
    R = Point(row=0, col=1)
    D = Point(row=1, col=0)
    L = Point(row=0, col=-1)

curr_pos = Point(0,0)
vertices = [curr_pos]
perimeter = 0

for line in lines:
    move = Direction[line.split()[0]]
    dist = int(line.split()[1])
    color = line.split()[2][2:-1]
    
    curr_pos += (move.value * dist)
    perimeter += dist
    vertices.append(curr_pos)

# Shoelace theorem for area
shoelace = 0
for i in range(len(vertices) - 1):
    x1, y1 = vertices[i].row, vertices[i].col
    x2, y2 = vertices[i + 1].row, vertices[i + 1].col
    shoelace += (x1 * y2) - (x2 * y1)

shoelace = abs(shoelace // 2)
excavated = shoelace + perimeter // 2 + 1

print('Excavated edge {} and total area {}'.format(perimeter, excavated))