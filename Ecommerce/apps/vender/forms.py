from apps.store.models import Product
from django.forms import ModelForm

class productForm(ModelForm):
    class Meta:
        model = Product
        fields= ['title','slug','description','price']
