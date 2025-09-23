from beautiful_dsa_algos_coding_interviews.trees.binary_tree.invert_binary_tree_iterative import TreeNode


class LRUCache:
    """
    LRU cache: O(1) amortized get/put using dict + doubly linked list.
    Uses TreeNode as a generic node and adds `.key`, `.val`, `.prev`, `.next`.
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
        """Insert node right after head (make it MRU)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: TreeNode) -> None:
        """Unlink node from the list."""
        prev, nxt = node.prev, node.next
        # Guard in case someone calls on a detached node
        if prev is not None:
            prev.next = nxt
        if nxt is not None:
            nxt.prev = prev
        node.prev = None
        node.next = None

    def _move_to_front(self, node: TreeNode) -> None:
        """Make an existing node MRU."""
        self._remove_node(node)
        self._add_to_front(node)

    def _evict_if_needed(self) -> None:
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
