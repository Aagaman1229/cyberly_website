from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    cover_image = models.ImageField(upload_to='main/covers/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title