from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'Сытый барин - Главная'
#     }
#     return render(request, 'catalog/home.html', context)

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Сытый барин - Главная'
    }

def contacts(request):
    context = {
        'title': 'Сытый барин - Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


# def product(request, pk):
#     products_list = Product.objects.get(pk=pk)
#     context = {
#         'object_list': products_list,
#         'title': 'Сытый барин - Информация о продукте'
#     }
#     return render(request, 'catalog/product_detail.html', context)


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Сытый барин - Информация о продукте'
    }


