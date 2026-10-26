from rest_framework import serializers
from .models import SavedArticle
class ArticleInputSerializer(serializers.Serializer):
 title=serializers.CharField(max_length=500); content=serializers.CharField(max_length=30000); url=serializers.URLField(required=False,allow_blank=True); source=serializers.CharField(required=False,allow_blank=True,max_length=255); mode=serializers.ChoiceField(choices=['brief','detailed'],default='brief')
class ResearchReportSerializer(serializers.Serializer):
 query=serializers.CharField(max_length=300); articles=serializers.ListField(child=serializers.DictField(),min_length=1,max_length=20)
class SavedArticleSerializer(serializers.ModelSerializer):
 class Meta:
  model=SavedArticle; fields=['id','title','url','source','description','published_at','created_at']; read_only_fields=['id','created_at']
