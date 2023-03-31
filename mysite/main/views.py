from django.shortcuts import render, redirect
from .models import HomeSlider, HomeSliderActive, Category, SubCategory
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm


def index(request):
    tertox_slider = HomeSliderActive.objects.all()[0]
    mnacac_sliderner = HomeSlider.objects.all()
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index.html', context={
        'tertox_slider':tertox_slider,
        'mnacac_sliderner':mnacac_sliderner,
        'category_list':category_list,
        'sub_category_list':sub_category_list,
	    'luys':'index'

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

def contact(request):
    return render(request,"main/contact-us.html", context={
	    'luys':'contact'
    })



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	error = ''
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			error = "Invalid username or password."
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form, 'error':error})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")