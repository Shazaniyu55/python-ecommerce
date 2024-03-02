from django.db.models import Count
from django.shortcuts import render
from . models import Product
from django.views import View

# Create your views here.
def home(request):
    return render(request, "app/home.html")



class CategoryView(View):
    def get(self, requet, val):
        product = Product.objects.filter(category = val)
        title = Product.objects.filter(category = val).values('title').annotate(total = Count('title'))
        return render(requet, 'app/category.html', locals())