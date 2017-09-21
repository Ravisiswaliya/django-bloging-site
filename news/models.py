from django.db import models

# Create your models here.
class Cat(models.Model):
    ctgry = models.CharField(max_length=200)

    def __str__(self):
        return self.ctgry

class News(models.Model):
    nc = models.ForeignKey(Cat, null=True,blank=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(blank=True,null=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

