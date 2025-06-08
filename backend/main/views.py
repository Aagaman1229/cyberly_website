from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by('-published_at')
    serializer_class = ArticleSerializer

    """// React Example
function ArticleDetail({ slug }) {
  const [article, setArticle] = useState(null);

  useEffect(() => {
    fetch(`/api/articles/${slug}/`)
      .then(res => res.json())
      .then(data => setArticle(data));
  }, [slug]);

  return article ? (
    <div>
      <h1>{article.title}</h1>
      <img src={article.cover_image} alt="cover" />
      <div dangerouslySetInnerHTML={{ __html: article.content }} />
    </div>
  ) : <p>Loading...</p>;
}"""