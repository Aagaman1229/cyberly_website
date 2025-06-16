# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Articles
from .serializers import ArticleSummarySerializer, ArticleDetailSerializer

@api_view(['GET'])
def article_list(request):
    objs = Articles.objects.all()
    serializer = ArticleSummarySerializer(objs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, slug):
    try:
        obj = Articles.objects.get(slug=slug)
        serializer = ArticleDetailSerializer(obj)
        return Response(serializer.data)
    except Articles.DoesNotExist:
        return Response({"error": "Article not found"}, status=404)
