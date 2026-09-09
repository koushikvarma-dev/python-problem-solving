from src.problems import LRUCache, longest_unique_substring, merge_intervals, shortest_path


def test_longest_unique_substring():
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1


def test_merge_intervals():
    assert merge_intervals([[1, 3], [2, 6], [8, 10]]) == [[1, 6], [8, 10]]


def test_shortest_path():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert shortest_path(graph, "A", "D") == ["A", "B", "D"]


def test_lru_cache():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    assert cache.get("b") is None
    assert cache.get("c") == 3
