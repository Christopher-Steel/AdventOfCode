from dataclasses import dataclass
from typing import List

@dataclass
class GraphNode:
    value: int
    distance_from_goal: int
    links: List["GraphNode"]