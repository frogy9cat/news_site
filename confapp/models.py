from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField(blank=True)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category1 = models.ForeignKey('Category1', models.CASCADE)
    is_bool = models.BooleanField(default=True)
    views = models.IntegerField(default=0, verbose_name='Korinishlar')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Information'
        verbose_name_plural = 'Informations'
        ordering = ['created_at']



class Category1(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'infos'





class Authorization(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True)
    password = models.IntegerField()
    is_bool = models.BooleanField(default=True)