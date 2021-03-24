from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DeleteView, FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from core.models import Product
from core.forms import ProductForm
from core.mixin import StaffRequiredMixin

class ProductListView(StaffRequiredMixin, ListView):
    model = Product
    template_name = 'product/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('product_create')
        context['list_url'] = reverse_lazy('product_list')
        context['entity'] = 'Porductos'
        return context

class ProductCreateView(StaffRequiredMixin, CreateView):
    model= Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('product_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Productos'
        context['list_url'] = reverse_lazy('product_list')
        context['entity'] = 'Productos'
        context['action'] = 'add'
        return context

class ProductUpdateView(StaffRequiredMixin, UpdateView):
    template_name = 'product/create.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('product_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Producto'
        context['entity'] = 'Producto'
        context['list_url'] = reverse_lazy('product_list')
        context['action'] = 'edit'
        print (context)
        return context

class ProductDeleteView(StaffRequiredMixin, DeleteView):
    template_name = 'product/delete.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('product_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Elimición de una Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('product_list')
        return context

# Esta clase verificara si mi formulario es valido y me reotara un url de exito 
class ProductformView(StaffRequiredMixin, FormView):
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('product_list')
    
    def form_valid(self, form):
        print (form.is_valid())
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'form | Product'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('product_list')
        return context

    