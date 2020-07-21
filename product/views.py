from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetail(DeleteView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreate(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully created!"
    template_name = 'product_form.html'

class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully updated!"
    template_name = 'product_form.html'

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully deleted!"
    template_name = 'product_confirm_delete.html'