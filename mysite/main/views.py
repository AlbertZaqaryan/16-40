from django.shortcuts import render
from .models import HomeSlider, HomeSliderActive, Category, SubCategory
# Create your views here.


def index(request):
    tertox_slider = HomeSliderActive.objects.all()[0]
    mnacac_sliderner = HomeSlider.objects.all()
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index.html', context={
        'tertox_slider':tertox_slider,
        'mnacac_sliderner':mnacac_sliderner,
        'category_list':category_list,
        'sub_category_list':sub_category_list

    })

def index_detail(request, id):
    tertox_slider = HomeSliderActive.objects.all()[0]
    mnacac_sliderner = HomeSlider.objects.all()
    category_list = Category.objects.all()
    category_list_count = SubCategory.objects.all()
    sub_category_list = Category.objects.filter(pk=id)
    return render(request, 'main/index_detail.html', context={
        'tertox_slider':tertox_slider,
        'mnacac_sliderner':mnacac_sliderner,
        'category_list':category_list,
        'sub_category_list':sub_category_list,
        'category_list_count':category_list_count

    })