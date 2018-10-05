from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class Blog1(models.Model):
    title = models.CharField("Title", max_length=50),
    written_date = models.DateTimeField("Written", auto_now_add=True),
    author_name = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title