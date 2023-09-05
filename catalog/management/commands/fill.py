from django.core.management.base import BaseCommand
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаляем старые записи
        Product.objects.all().delete()

        # Заполняем базу новыми данными
        new_products = [
            Product(name='Котлеты куриные', description='Котлеты из мяса курицы 1 сорт', category_id='2', price='300', date_create='2023-09-05', date_last_change='2023-09-05'),
            Product(name='Йогурт с земляникой', description='Йогурт жирностью 5% с добавлением земляники', category_id='1', price='80', date_create='2023-09-05', date_last_change='2023-09-05'),
            Product(name='Черный чай', description='Черный байховый чай листовой', category_id='3', price='200', date_create='2023-09-05', date_last_change='2023-09-05'),
            Product(name='Булочка "Маковка"', description='Булочка из муки высшего сорта с маком и сахаром', category_id='4', price='30', date_create='2023-09-05', date_last_change='2023-09-05'),
        ]
        Product.objects.bulk_create(new_products)