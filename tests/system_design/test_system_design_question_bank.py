import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from system_design.question_bank import (
    QUESTION_BANK,
    filter_by_category,
    filter_by_difficulty,
    get_question_by_slug,
    list_categories,
    render_markdown_study_guide,
    search_questions,
)


def test_question_bank_has_good_size():
    assert len(QUESTION_BANK) >= 30


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
    assert "caching" in categories
    assert "reliability" in categories


def test_filter_by_category_hits_expected_group():
    caching_items = filter_by_category("caching")
    assert caching_items
    assert all(item.category == "caching" for item in caching_items)


def test_filter_by_difficulty_hits_expected_group():
    hard_items = filter_by_difficulty("hard")
    assert hard_items
    assert all(item.difficulty == "hard" for item in hard_items)


def test_search_questions_by_keyword():
    results = search_questions("cache")
    assert results
    assert any("cache" in item.question.lower() or "cache" in item.deep_dive.lower() for item in results)


def test_search_questions_empty_term_returns_all():
    assert search_questions("") == QUESTION_BANK


def test_get_question_by_slug_found():
    item = get_question_by_slug("cache-invalidation")
    assert item is not None
    assert item.category == "caching"
    assert item.difficulty == "medium"


def test_get_question_by_slug_missing():
    assert get_question_by_slug("not-a-real-question") is None


def test_render_markdown_study_guide_contains_sections():
    markdown = render_markdown_study_guide()
    assert markdown.startswith("# System Design Question Bank")
    assert "## Fundamentals" in markdown
    assert "## Caching" in markdown
    assert "### Why is cache invalidation considered hard?" in markdown


def test_render_markdown_contains_all_categories():
    markdown = render_markdown_study_guide()
    for category in list_categories():
        heading = f"## {category.replace('-', ' ').title()}"
        assert heading in markdown
