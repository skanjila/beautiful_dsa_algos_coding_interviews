import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from data_science.practical_question_bank import (
    PRACTICAL_QUESTION_BANK,
    filter_by_category,
    filter_by_difficulty,
    get_question_by_slug,
    list_categories,
    render_markdown_study_guide,
    search_questions,
)


def test_practical_question_bank_has_good_size():
    assert len(PRACTICAL_QUESTION_BANK) >= 6


def test_practical_question_bank_slugs_are_unique():
    slugs = [entry.slug for entry in PRACTICAL_QUESTION_BANK]
    assert len(slugs) == len(set(slugs))


def test_every_entry_has_required_content():
    for entry in PRACTICAL_QUESTION_BANK:
        assert entry.slug
        assert entry.category
        assert entry.difficulty in {"easy", "medium", "hard"}
        assert len(entry.question) > 20
        assert len(entry.interview_approach) > 30
        assert len(entry.pandas_approach) > 20
        assert len(entry.python_ml_approach) > 20
        assert len(entry.deep_dive) > 40


def test_category_listing_and_filtering():
    categories = list_categories()
    assert categories == sorted(categories)
    assert "feature-engineering" in categories
    items = filter_by_category("feature-engineering")
    assert items
    assert all(item.category == "feature-engineering" for item in items)


def test_filter_by_difficulty():
    items = filter_by_difficulty("medium")
    assert items
    assert all(item.difficulty == "medium" for item in items)


def test_search_questions():
    results = search_questions("pipeline")
    assert results
    assert any(
        "pipeline" in item.question.lower()
        or "pipeline" in item.python_ml_approach.lower()
        for item in results
    )


def test_get_question_by_slug():
    item = get_question_by_slug("time-window-features")
    assert item is not None
    assert item.category == "feature-engineering"


def test_render_markdown_contains_expected_sections():
    markdown = render_markdown_study_guide()
    assert markdown.startswith("# Data Science Practical Interview Problems")
    assert "## Feature Engineering" in markdown
    assert "Python/ML approach:" in markdown
