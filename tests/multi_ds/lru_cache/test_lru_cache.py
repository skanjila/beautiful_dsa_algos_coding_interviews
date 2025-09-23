# tests/cache/test_lru_cache.py
import pytest

from beautiful_dsa_algos_coding_interviews.multi_ds.lru_cache import LRUCache


def dll_keys_from_mru_to_lru(cache: LRUCache):
    """
    Inspect order in the internal doubly linked list:
    returns a list of node keys from most recent (after head) to least (before tail).
    Supports either node.key or node.val as the lookup key (handles both).
    """
    keys = []
    cur = cache.head.next
    # safety: hard stop in case of future pointer bugs
    seen = 0
    while cur is not cache.tail:
        k = getattr(cur, "key", None)
        if k is None:
            k = getattr(cur, "val", None)
        keys.append(k)
        cur = cur.next
        seen += 1
        assert seen <= len(cache.cache), "Cycle detected or DLL corruption"
    return keys


# -------------------------
# Construction / validation
# -------------------------

def test_capacity_must_be_positive():
    with pytest.raises(ValueError):
        LRUCache(0)
    with pytest.raises(ValueError):
        LRUCache(-3)


# -------------------------
# Basic semantics
# -------------------------

def test_get_miss_returns_minus_one_and_no_side_effects():
    cache = LRUCache(capacity=2)
    assert cache.get(42) == -1
    # still empty (no nodes between sentinels)
    assert dll_keys_from_mru_to_lru(cache) == []


def test_put_and_get_hit():
    cache = LRUCache(capacity=2)
    cache.put(1, 100)
    cache.put(2, 200)
    assert cache.get(1) == 100
    assert cache.get(2) == 200


def test_put_updates_value_and_recency():
    cache = LRUCache(capacity=2)
    cache.put(1, 100)
    cache.put(2, 200)
    # Update existing key; value changes and it becomes MRU
    cache.put(1, 111)
    assert cache.get(1) == 111
    assert dll_keys_from_mru_to_lru(cache) == [1, 2]


def test_get_hit_updates_recency():
    cache = LRUCache(capacity=2)
    cache.put(1, 100)
    cache.put(2, 200)
    assert cache.get(1) == 100  # 1 becomes MRU
    assert dll_keys_from_mru_to_lru(cache) == [1, 2]


def test_repeated_gets_keep_item_as_mru():
    cache = LRUCache(capacity=3)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.put(3, 30)
    # 2 -> MRU, then again
    assert cache.get(2) == 20
    assert cache.get(2) == 20
    assert dll_keys_from_mru_to_lru(cache) == [2, 3, 1]


# -------------------------
# Eviction behavior
# -------------------------

def test_eviction_of_lru_on_capacity_two():
    cache = LRUCache(capacity=2)
    cache.put(1, 100)
    cache.put(2, 200)
    # Access 1 to make it MRU; 2 becomes LRU
    assert cache.get(1) == 100
    # Insert 3 -> evict key 2
    cache.put(3, 300)
    assert cache.get(2) == -1
    assert cache.get(1) == 100
    assert cache.get(3) == 300
    assert dll_keys_from_mru_to_lru(cache) == [3, 1]

