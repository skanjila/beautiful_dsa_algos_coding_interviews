import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from data_engineering.question_bank import (
    QUESTION_BANK,
    filter_by_category,
    filter_by_difficulty,
    get_question_by_slug,
    list_categories,
    render_markdown_study_guide,
    search_questions,
)


def test_question_bank_has_good_size():
    assert len(QUESTION_BANK) >= 15


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
    assert "fundamentals" in categories
    assert "storage" in categories


def test_filter_by_category_hits_expected_group():
    items = filter_by_category("storage")
    assert items
    assert all(item.category == "storage" for item in items)


def test_filter_by_difficulty_hits_expected_group():
    items = filter_by_difficulty("hard")
    assert items
    assert all(item.difficulty == "hard" for item in items)


def test_search_questions_by_keyword():
    results = search_questions("stream")
    assert results
    assert any("stream" in item.question.lower() or "stream" in item.deep_dive.lower() for item in results)


def test_search_questions_empty_term_returns_all():
    assert search_questions("") == QUESTION_BANK


def test_get_question_by_slug_found():
    item = get_question_by_slug("cdc")
    assert item is not None
    assert item.category == "ingestion"


def test_get_question_by_slug_missing():
    assert get_question_by_slug("not-real") is None


def test_render_markdown_contains_expected_sections():
    markdown = render_markdown_study_guide()
    assert markdown.startswith("# Data Engineering Question Bank")
    assert "## Fundamentals" in markdown
    assert "## Storage" in markdown
