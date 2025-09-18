import pytest

# If the function lives in another module, change the import accordingly, e.g.:
# from your_module import can_finish_kahn
from beautiful_dsa_algos_coding_interviews.graphs.can_finish import can_finish_kahn  # <-- update this to your module name


@pytest.mark.parametrize(
    "num_courses, prerequisites, expected",
    [
        # 1) No prerequisites: always possible
        (1, [], True),
        (5, [], True),

        # 2) Simple linear chain: 0<-1<-2<-3 (prereq pairs [course, prereq])
        # Meaning: to take 3 you need 2; to take 2 you need 1; to take 1 you need 0
        (4, [[1, 0], [2, 1], [3, 2]], True),

        # 3) Simple cycle: 0<-1 and 1<-0
        (2, [[1, 0], [0, 1]], False),

        # 4) Self-loop cycle: 0<-0
        (1, [[0, 0]], False),

        # 5) Disconnected DAG: two components, both acyclic
        (6, [[2, 1], [1, 0], [5, 4]], True),

        # 6) Diamond-shaped DAG:
        #    0 -> 1 -> 3
        #     \> 2 ->/
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),

        # 7) Cycle inside a larger graph: component {0,1,2} has a cycle; others are fine
        (6, [[1, 0], [2, 1], [0, 2], [4, 3], [5, 4]], False),
    ],
)
def test_can_finish_kahn_parametrized(num_courses, prerequisites, expected):
    assert can_finish_kahn(num_courses, prerequisites) is expected


def test_large_acyclic_chain():
    # Long acyclic chain should be True
    n = 1000
    prereqs = [[i, i - 1] for i in range(1, n)]
    assert can_finish_kahn(n, prereqs) is True


def test_large_single_cycle():
    # Large single cycle over all nodes should be False
    n = 500
    prereqs = [[(i + 1) % n, i] for i in range(n)]
    assert can_finish_kahn(n, prereqs) is False
