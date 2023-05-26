from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255)

class Resource(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=255)
    url = models.URLField()
