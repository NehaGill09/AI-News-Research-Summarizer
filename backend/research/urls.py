from django.urls import path
from .views import NewsSearchView,SummarizeView,ResearchReportView,SavedArticleListCreateView,SavedArticleDeleteView
urlpatterns=[path('news/search/',NewsSearchView.as_view()),path('research/summarize/',SummarizeView.as_view()),path('research/report/',ResearchReportView.as_view()),path('saved/',SavedArticleListCreateView.as_view()),path('saved/<int:pk>/',SavedArticleDeleteView.as_view())]
