from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['version_is_active'] = Version.objects.filter(is_current_version=True)
        return context


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Сытый барин - Информация о продукте'
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data().get('formset')
        if formset.is_valid():
            count_is_сurrent_version = 0
            for f in formset:
                if formset.can_delete and formset._should_delete_form(f):
                    continue
                if f.cleaned_data.get('is_сurrent_version'):
                    count_is_сurrent_version += 1
                    if count_is_сurrent_version > 1:
                        form.add_error(None, "Не может быть больше одной текущей версии")
                        return self.form_invalid(form=form)
            formset.save()
            return super().form_valid(form=form)




class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')