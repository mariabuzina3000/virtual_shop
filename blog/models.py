from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', null=True, blank=True)
    date_create = models.DateField(verbose_name='дата создания')

    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    count_views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
