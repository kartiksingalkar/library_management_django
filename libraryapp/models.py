from django.db import models

# Create your models here.

class Books(models.Model):
    book_id = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
