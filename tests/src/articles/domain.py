from typing import Optional

from src.articles.domain import ArticleRepository, Article, ArticleId


class FakeArticleRepository(ArticleRepository):
    def __init__(self) -> None:
        self._articles = {}

    def find(self, id: ArticleId) -> Optional[Article]:
        return self._articles.get(id.value, None)

    def save(self, article: Article) -> None:
        self._articles[article.id.value] = article
