import abc
from typing import Optional

import pydantic

class ArticleTitleBlankError(Exception):
    ...


class ArticleBodyBlankError(Exception):
    ...


class ArticleIdBlankError(Exception):
    ...


class ArticleNotFoundError(Exception):
    ...


class ArticleId(pydantic.BaseModel):
    value: str

    @pydantic.validator("value")
    def ensure_id_not_blank(cls, value: str) -> str:
        if value == "":
            raise ArticleIdBlankError()

        return value


class ArticleTitle(pydantic.BaseModel):
    value: str

    @pydantic.validator("value")
    def ensure_title_not_blank(cls, value: str) -> str:
        if value == "":
            raise ArticleTitleBlankError()

        return value


class ArticleBody(pydantic.BaseModel):
    value: str

    @pydantic.validator("value")
    def ensure_body_not_blank(cls, value: str) -> str:
        if value == "":
            raise ArticleBodyBlankError()

        return value


class Article:

    def __init__(
        self,
        id: ArticleId,
        title: ArticleTitle,
        body: ArticleBody,
    ) -> None:
        self.id = id
        self.title = title
        self.body = body

    @classmethod
    def create(cls, id: str, title: str, body: str) -> "Article":
        return cls(
            ArticleId(value=id),
            ArticleTitle(value=title),
            ArticleBody(value=body)
        )

    def to_dict(self) -> dict:
        return dict(
            id=self.id.value,
            title=self.title.value,
            body=self.body.value
        )


class ArticleRepository(abc.ABC):
    @abc.abstractmethod
    def find(self, id: ArticleId) -> Optional[Article]:
        raise NotImplementedError()

    @abc.abstractmethod
    def save(self, article: Article) -> None:
        raise NotImplementedError()


class ArticleFinder:
    def __init__(self, repo: ArticleRepository, id: str) -> None:
        self._repo = repo
        self._id = ArticleId(value=id)

    def execute(self) -> Article:
        article = self._repo.find(id=self._id)

        if article is None:
            raise ArticleNotFoundError()

        return article
