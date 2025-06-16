from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Research
from .serializers import ResearchSerializer

@api_view(['GET'])
def research_list(request):
    objs = Research.objects.all().order_by('-published_at')
    serializer = ResearchSerializer(objs, many=True)
    return Response(serializer.data)