from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        permissions = (
            ('can_edit_article', 'Can edit article'),
            ('can_delete_article', 'Can delete article'),
        )

    def __str__(self):
        return self.title