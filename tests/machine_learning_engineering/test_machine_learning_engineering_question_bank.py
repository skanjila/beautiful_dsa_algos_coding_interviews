import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from machine_learning_engineering.question_bank import (
    QUESTION_BANK,
    filter_by_category,
    filter_by_difficulty,
    get_question_by_slug,
    list_categories,
    render_markdown_study_guide,
    search_questions,
)


def test_question_bank_has_good_size():
    assert len(QUESTION_BANK) >= 20


def test_question_bank_slugs_are_unique():
    slugs = [entry.slug for entry in QUESTION_BANK]
    assert len(slugs) == len(set(slugs))


def test_every_entry_has_required_content():
    for entry in QUESTION_BANK:
        assert entry.slug
        assert entry.category
        assert entry.difficulty in {"easy", "medium", "hard"}
        assert len(entry.question) > 20
        assert len(entry.short_answer) > 20
        assert len(entry.deep_dive) > 40


def test_list_categories_sorted_and_nonempty():
    categories = list_categories()
    assert categories == sorted(categories)
    assert "coding" in categories
    assert "ml-system-design" in categories
    assert "llm-genai" in categories


def test_filter_by_category_hits_expected_group():
    items = filter_by_category("ml-system-design")
    assert items
    assert all(item.category == "ml-system-design" for item in items)


def test_filter_by_difficulty_hits_expected_group():
    items = filter_by_difficulty("hard")
    assert items
    assert all(item.difficulty == "hard" for item in items)


def test_search_questions_by_keyword():
    results = search_questions("ranking")
    assert results
    assert any("ranking" in item.question.lower() or "ranking" in item.deep_dive.lower() for item in results)


def test_search_questions_empty_term_returns_all():
    assert search_questions("") == QUESTION_BANK


def test_get_question_by_slug_found():
    item = get_question_by_slug("recommendation-funnel")
    assert item is not None
    assert item.category == "ml-system-design"


def test_get_question_by_slug_missing():
    assert get_question_by_slug("not-real") is None


def test_render_markdown_contains_expected_sections():
    markdown = render_markdown_study_guide()
    assert markdown.startswith("# Machine Learning Engineering Question Bank")
    assert "## Coding" in markdown
    assert "## Ml System Design" in markdown
