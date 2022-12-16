import domain
import commons


class CreateArticleRequest(commons.Request):
    id: str
    title: str
    body: str


def create_article(
    request: CreateArticleRequest,
    repository: domain.ArticleRepository,
) -> None:
    _ensure_article_not_exist(repository=repository, id=request.id)

    article = domain.Article.create(id=request.id, title=request.title, body=request.body)

    repository.save(article)


def _ensure_article_not_exist(repository: domain.ArticleRepository, id: str) -> None:
    id = domain.ArticleId(value=id)
    article = repository.search(id)
    if article is not None:
        raise domain.ArticleAlreadyExistError()