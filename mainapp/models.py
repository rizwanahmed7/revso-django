from django.db import models

# Create your models here.
class Subject(models.Model):
    Subject_name = models.CharField(max_length=100)
    Discription = models.CharField(max_length=100)
    def _str_(self):
        return self.pk
    
    
class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic = models.CharField(max_length=300)
    content =  models.CharField(max_length=100)
    def _str_(self):
        return self.pk
