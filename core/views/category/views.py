from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DeleteView, FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from core.models import Category
from core.forms import CategoryForm
from core.mixin import StaffRequiredMixin
# Create your views here.

class CategoryListView(StaffRequiredMixin, ListView):
    model = Category
    template_name = 'category/list.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            acttion = request.POST['action']
            if acttion =='searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('category_create')
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Categorías'
        return context

class CategoryCreateView(StaffRequiredMixin, CreateView):
    model= Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Categorías'
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Categorías'
        context['action'] = 'add'
        return context

class CategoryUpdateView(StaffRequiredMixin, UpdateView):
    template_name = 'category/create.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('category_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'edit'
        return context

class CategoryDeleteView(StaffRequiredMixin, DeleteView):
    template_name = 'category/delete.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Elimición de una Categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('category_list')
        return context

# Esta clase verificara si mi formulario es valido y me reotara un url de exito 
class CategoryformView(StaffRequiredMixin, FormView):
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')
    

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
        context['title'] = 'form | Categorty'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('category_list')
        return context

    