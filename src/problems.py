"""Practical algorithmic problem-solving examples."""

from collections import OrderedDict, deque


def longest_unique_substring(s: str) -> int:
    """Return the length of the longest substring with unique characters."""
    left = 0
    best = 0
    last_seen = {}
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


def merge_intervals(intervals):
    """Merge overlapping inclusive intervals."""
    if not intervals:
        return []
    result = []
    for start, end in sorted(intervals):
        if not result or start > result[-1][1]:
            result.append([start, end])
        else:
            result[-1][1] = max(result[-1][1], end)
    return result


def shortest_path(graph, start, target):
    """Return the shortest unweighted path using BFS."""
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


class LRUCache:
    """Small fixed-size LRU cache backed by OrderedDict."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._data = OrderedDict()

    def get(self, key, default=None):
        if key not in self._data:
            return default
        value = self._data.pop(key)
        self._data[key] = value
        return value

    def put(self, key, value):
        if key in self._data:
            self._data.pop(key)
        self._data[key] = value
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)
