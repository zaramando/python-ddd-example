import pytest

from src.articles.application import ArticleCreator
from src.articles.domain import (
    ArticleTitleBlankError,
    ArticleFinder,
    ArticleNotFoundError,
    ArticleBodyBlankError,
    ArticleIdBlankError,
)
from tests.src.articles.domain import FakeArticleRepository


@pytest.mark.unittest
def test_should_not_create_an_article_with_a_blank_title() -> None:
    id = "1"
    title = ""
    body = "Some Body"

    repo = FakeArticleRepository()
    finder = ArticleFinder(repo=repo, id=id)

    with pytest.raises(ArticleTitleBlankError):
        ArticleCreator(repo=repo, id=id, title=title, body=body).execute()
    with pytest.raises(ArticleNotFoundError):
        finder.execute()


@pytest.mark.unittest
def test_should_create_an_article() -> None:
    id = "1"
    title = "Some Title"
    body = "Some Body"

    expeted = {"id": id, "title": title, "body": body}

    repo = FakeArticleRepository()
    finder = ArticleFinder(repo=repo, id=id)

    ArticleCreator(repo=repo, id=id, title=title, body=body).execute()

    assert expeted == finder.execute().to_dict()


@pytest.mark.unittest
def test_should_not_create_an_article_with_a_blank_body() -> None:
    id = "1"
    title = "Some Title"
    body = ""
    repo = FakeArticleRepository()

    with pytest.raises(ArticleBodyBlankError):
        ArticleCreator(repo=repo, id=id, title=title, body=body).execute()


@pytest.mark.unittest
def test_should_not_create_an_article_with_a_blank_id() -> None:
    id = ""
    title = "Some Title"
    body = "Some Body"
    repo = FakeArticleRepository()

    with pytest.raises(ArticleIdBlankError):
        ArticleCreator(repo=repo, id=id, title=title, body=body).execute()
