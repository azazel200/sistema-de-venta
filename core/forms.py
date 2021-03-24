from django.forms import *
from datetime import datetime
from core.models import Category, Product, Client, Sale

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'Off'
        self.fields['name'].widget.attrs['autocfocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',  
                }
            ),
             'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese la descripción',
                    'rows': 3,
                    'cols': 4 
                }
            ),
        }
        exclude = ['user_creation', 'user_updated']

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'Off'
        self.fields['name'].widget.attrs['autocfocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }

class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control'
    }))

    products = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control'
    })) 

class ClientForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'Off'
        self.fields['name'].widget.attrs['autocfocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese sus nombres',
                }
            ),
            'surnames' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese sus apellidos',
                }
            ),
            'dni' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese su DNI',
                }
            ),
            'date_birthday' : DateInput(format='%Y-%m-%d',
                attrs={
                    'value' : datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'address' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese su dirección',
                }
            ),
            'gender' : Select()
        }
        exclude = ['user_update', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data