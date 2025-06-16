from rest_framework import serializers
from .models import Articles

class ArticleSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['id', 'title','slug', 'published_at', 'cover_image']

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'