from src.articles.domain import Article, ArticleRepository


class ArticleCreator:
    def __init__(self, repo: ArticleRepository, id: str, title: str, body: str) -> None:
        self._repo = repo
        self.id = id
        self.title = title
        self.body = body

    def execute(self) -> None:
        article = Article.create(id=self.id, title=self.title, body=self.body)

        self._repo.save(article)
