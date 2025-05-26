import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from lib.models import Author, Magazine, Article

def test_author_name():
    author = Author("Teresa")
    assert author.name == "Teresa"

def test_magazine_name_and_category():
    mag = Magazine("Tech Weekly", "Technology")
    assert mag.name == "Tech Weekly"
    assert mag.category == "Technology"

def test_article_creation():
    author = Author("James")
    mag = Magazine("Dev News", "Development")
    article = Article(author, mag, "Writing Clean Code")

    assert article.title == "Writing Clean Code"
    assert article.author == author
    assert article.magazine == mag

def test_duplicate_article_title_for_same_author():
    author = Author("Alice")
    mag = Magazine("Design Daily", "Design")
    Article(author, mag, "UI Trends 2025")

    with pytest.raises(ValueError):
        Article(author, mag, "UI Trends 2025")

def test_magazine_contributors_and_titles():
    author = Author("Sam")
    mag = Magazine("Creative Minds", "Art")
    Article(author, mag, "The Art of Simplicity")
    assert mag.contributors() == [author]
    assert mag.article_titles() == ["The Art of Simplicity"]
