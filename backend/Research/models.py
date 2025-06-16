from django.db import models

# Create your models here.
class Research(models.Model):
    journal = models.CharField(max_length=255)
    link = models.URLField()  # for external link to the paper
    image = models.ImageField(upload_to='research/images/', blank=True, null=True)
    published_at = models.DateField()
    description = models.TextField(blank=True, null=True)  # optional

    def __str__(self):
        return self.journal