from beautiful_dsa_algos_coding_interviews.trees.binary_tree.binary_tree_level_order import level_order
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.serialize_deserialize_binary_tree import Codec
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def test_serialize_deserialize_round_trip():
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialized = codec.serialize(root)
    restored = codec.deserialize(serialized)
    assert level_order(restored) == [[1], [2, 3], [4, 5]]


def test_serialize_deserialize_empty_tree():
    codec = Codec()
    assert codec.deserialize(codec.serialize(None)) is None
