from beautiful_dsa_algos_coding_interviews.trees.binary_tree.invert_binary_tree_iterative import TreeNode


class LRUCache:
    """
    LRU cache: O(1) amortized get/put because the dictionary finds nodes by key
    directly and the doubly linked list updates recency with pointer rewiring.
    Uses TreeNode as a generic node and adds `.key`, `.val`, `.prev`, `.next`.

    Space complexity: O(capacity) because the cache stores at most ``capacity``
    nodes and a matching dictionary entry for each.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = TreeNode(0)  # dummy head
        self.tail = TreeNode(0)  # dummy tail
        # Ensure dummy nodes have prev/next
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def _add_to_front(self, node: TreeNode) -> None:
        """Insert node right after head (make it MRU).

        Time complexity: O(1)
        Space complexity: O(1)
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: TreeNode) -> None:
        """Unlink node from the list.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        prev, nxt = node.prev, node.next
        # Guard in case someone calls on a detached node
        if prev is not None:
            prev.next = nxt
        if nxt is not None:
            nxt.prev = prev
        node.prev = None
        node.next = None

    def _move_to_front(self, node: TreeNode) -> None:
        """Make an existing node MRU.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self._remove_node(node)
        self._add_to_front(node)

    def _evict_if_needed(self) -> None:
        """Evict the least recently used node if capacity is exceeded.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if len(self.cache) > self.capacity:
            # LRU node is right before tail
            lru = self.tail.prev
            # Safety: lru should never be a dummy
            if lru is self.head:
                return
            self._remove_node(lru)
            del self.cache[lru.key]

    def get(self, key: int) -> int:
        """
        Return value if present; -1 otherwise.
        On hit: mark as most-recently used.
        On miss: DO NOT insert or evict.

        Time complexity: O(1) amortized
        Space complexity: O(1)
        """
        node = self.cache.get(key)
        if node is None:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Insert/update key with value.
        On update: write value and move to front.
        On insert: create node, insert at front, evict LRU if over capacity.

        Time complexity: O(1) amortized
        Space complexity: O(1) auxiliary
        """
        node = self.cache.get(key)
        if node is not None:
            node.val = value
            self._move_to_front(node)
            return

        # Create a fresh node; store both key and val explicitly
        node = TreeNode(value)
        node.key = key      # <-- important for eviction dictionary delete
        node.val = value    # <-- value to be returned by get()
        # Ensure `prev`/`next` exist on this TreeNode
        node.prev = None
        node.next = None

        self.cache[key] = node
        self._add_to_front(node)
        self._evict_if_needed()
