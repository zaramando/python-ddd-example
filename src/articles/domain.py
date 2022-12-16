import abc
from typing import Optional
import commons


class ArticleId(commons.ValueObject):
    value: str


class ArticleTitle(commons.ValueObject):
    value: str


class ArticleBody(commons.ValueObject):
    value: str


class ArticleCreated(commons.DomainEvent):
    id: str
    title: str
    body: str


class Article(commons.AggregateRoot):
    id: ArticleId
    title: ArticleTitle
    body: ArticleBody

    @classmethod
    def create(cls, id: str, title: str, body: str) -> "Article":
        article = cls(
            id=ArticleId(value=id),
            title=ArticleTitle(value=title),
            body=ArticleBody(value=body),
        )

        article.record_event(
            ArticleCreated(
                id=article.id.value,
                title=article.title.value,
                body=article.body.value,
            )
        )

        return article


class ArticleRepository(abc.ABC):
    @abc.abstractmethod
    def search(self, id: ArticleId) -> Optional[Article]:
        raise NotImplementedError()

    @abc.abstractmethod
    def save(self, article: Article) -> None:
        raise NotImplementedError()


class ArticleAlreadyExistError(Exception):
    ...
