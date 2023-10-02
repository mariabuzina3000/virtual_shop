from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    # created_at = models.CharField(max_length=15, verbose_name='наименование', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('id',)


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.CharField(max_length=250, verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', blank=True, null=True, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_create = models.DateField(verbose_name='дата создания')
    date_last_change = models.DateField(verbose_name='дата последнего изменения')


    def __str__(self):
        return f'{self.image} {self.name} {self.price}'


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('id',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number_version = models.CharField(max_length=20, verbose_name='номер версии')
    name_version = models.CharField(max_length=250, verbose_name='название версии')
    is_current_version = models.BooleanField(default=False, verbose_name='текущая версия')

    def __str__(self):
        return f'{self.version_name}'


    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'