from django.db import models

# Create your models here.
class Search(models.Model):
    searchword=models.TextField(max_length=1000)
    pagelocation=models.TextField(max_length=1000)
    viewname=models.TextField(max_length=1000, default='index',)

    def __str__(self):
        return self.searchword[:100]

class FeedbackMessage(models.Model):
    Name=models.TextField(max_length=100)
    Email=models.TextField(max_length=100)
    Message=models.TextField(max_length=100)

    def __str__(self):
        return self.Name[:10]