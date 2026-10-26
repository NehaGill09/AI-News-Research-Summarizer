from django.db import connection
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SavedArticle
from .serializers import ArticleInputSerializer,ResearchReportSerializer,SavedArticleSerializer
from .services import search_news,summarize_article,research_report
class HealthView(APIView):
 authentication_classes=[]; permission_classes=[permissions.AllowAny]
 def get(self,request):
  try: connection.ensure_connection(); db='ok'
  except Exception: db='unavailable'
  return Response({'status':'ok' if db=='ok' else 'degraded','database':db})
class NewsSearchView(APIView):
 def get(self,request):
  q=(request.query_params.get('q') or '').strip()
  if len(q)<2: return Response({'error':'Provide a search query of at least 2 characters.'},status=400)
  try: return Response(search_news(q,max(1,int(request.query_params.get('page',1))),min(50,max(1,int(request.query_params.get('page_size',10))))))
  except (ValueError,TypeError): return Response({'error':'page and page_size must be integers.'},status=400)
  except Exception: return Response({'error':'News provider request failed. Check API key and quota.'},status=502)
class SummarizeView(APIView):
 def post(self,request):
  s=ArticleInputSerializer(data=request.data); s.is_valid(raise_exception=True); d=s.validated_data
  try: return Response(summarize_article(d['title'],d['content'],d['mode']))
  except Exception: return Response({'error':'Summarization provider failed. Check configuration or retry.'},status=502)
class ResearchReportView(APIView):
 def post(self,request):
  s=ResearchReportSerializer(data=request.data); s.is_valid(raise_exception=True)
  try: return Response(research_report(s.validated_data['query'],s.validated_data['articles']))
  except Exception: return Response({'error':'Unable to generate report; check provider configuration.'},status=502)
class SavedArticleListCreateView(generics.ListCreateAPIView):
 serializer_class=SavedArticleSerializer; permission_classes=[permissions.IsAuthenticated]
 def get_queryset(self): return SavedArticle.objects.filter(user=self.request.user)
 def perform_create(self,serializer): serializer.save(user=self.request.user)
class SavedArticleDeleteView(generics.DestroyAPIView):
 serializer_class=SavedArticleSerializer; permission_classes=[permissions.IsAuthenticated]
 def get_queryset(self): return SavedArticle.objects.filter(user=self.request.user)
