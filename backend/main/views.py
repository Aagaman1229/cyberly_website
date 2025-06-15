from rest_framework.response import Response
from .models import Articles
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer

@api_view(['GET'])
def article(request):
    if request.method == 'GET':
        objs = Articles.objects.all()
        serializer = ArticleSerializer(objs, many = True)
        return Response(serializer.data)