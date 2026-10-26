from django.test import TestCase
from rest_framework.test import APIClient
from .services import canonical_key
class ResearchApiTests(TestCase):
 def setUp(self): self.client=APIClient()
 def test_health(self): self.assertEqual(self.client.get('/api/health/').status_code,200)
 def test_search_requires_query(self): self.assertEqual(self.client.get('/api/news/search/').status_code,400)
 def test_summary_fallback(self):
  r=self.client.post('/api/research/summarize/',{'title':'Example','content':'First sentence. Second sentence.','mode':'brief'},format='json'); self.assertEqual(r.status_code,200); self.assertEqual(r.data['method'],'extractive_fallback')
 def test_url_key_stable(self): self.assertEqual(canonical_key('https://example.com/story/'),canonical_key('https://example.com/story'))
