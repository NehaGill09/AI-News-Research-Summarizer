from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="SavedArticle",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=500)),
                ("url", models.URLField(max_length=1000)),
                ("source", models.CharField(blank=True, max_length=255)),
                ("description", models.TextField(blank=True)),
                ("published_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="saved_articles", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-created_at"], "constraints": [models.UniqueConstraint(fields=("user", "url"), name="unique_saved_article_per_user")]},
        ),
    ]
