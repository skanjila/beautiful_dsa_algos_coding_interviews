import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from machine_learning_engineering.practice_problems import (
    PRACTICE_PROBLEMS,
    list_sections,
    list_stubbed_problem_slugs,
)
from machine_learning_engineering import practice_stubs


def test_practice_problem_registry_has_good_size():
    assert len(PRACTICE_PROBLEMS) >= 10


def test_practice_problem_slugs_are_unique():
    slugs = [entry.slug for entry in PRACTICE_PROBLEMS]
    assert len(slugs) == len(set(slugs))


def test_sections_are_sorted_and_cover_llm():
    sections = list_sections()
    assert sections == sorted(sections)
    assert "llm-genai" in sections
    assert "ranking" in sections


def test_stubbed_problem_slugs_match_registry():
    stubbed = set(list_stubbed_problem_slugs())
    registry = {entry.slug for entry in PRACTICE_PROBLEMS if entry.status == "stubbed"}
    assert stubbed == registry


def test_stubbed_functions_exist():
    for entry in PRACTICE_PROBLEMS:
        assert hasattr(practice_stubs, entry.function_name)


def test_a_stubbed_function_raises_not_implemented():
    try:
        practice_stubs.compute_average_precision([1, 0, 1])
    except NotImplementedError:
        pass
    else:
        raise AssertionError("Expected NotImplementedError for contribution stub")
