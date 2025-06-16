from rest_framework import serializers
from .models import Research

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'  # or list specific fields like ['id', 'journal', 'link', 'image', 'published_at', 'description']
