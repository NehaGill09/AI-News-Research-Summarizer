from django.conf import settings
from django.db import models
class SavedArticle(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='saved_articles')
 title=models.CharField(max_length=500); url=models.URLField(max_length=1000); source=models.CharField(max_length=255,blank=True); description=models.TextField(blank=True); published_at=models.DateTimeField(null=True,blank=True); created_at=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=['-created_at']; constraints=[models.UniqueConstraint(fields=['user','url'],name='unique_saved_article_per_user')]
 def __str__(self): return self.title
