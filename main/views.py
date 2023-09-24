from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import F

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'npm': 2206826476,
        'kelas': 'PBP-A',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def lightcones(request):
    items = Item.objects.filter(user=request.user)
    jumlah_item = 0

    # Menghitung jumlah item berdasarkan amount
    for i in items.values():
        jumlah_item += i.get("amount")

    context = {
        'jumlah_item': jumlah_item,
        'items': items
    }

    return render(request, "lightcones.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:lightcones'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increase_amount(request, item_id):
    Item.objects.filter(user=request.user).filter(pk=item_id).update(amount=F('amount')+1)
    return HttpResponse('The amount has been increased by 1. Please go back and refresh the last page.')

def decrease_amount(request, item_id):
    Item.objects.filter(user=request.user).filter(pk=item_id).update(amount=F('amount')-1)
    return HttpResponse('The amount has been decreased by 1. Please go back and refresh the last page.')

def delete_item(request, item_id):
    Item.objects.filter(user=request.user).filter(pk=item_id).delete()
    return HttpResponse('The item has been deleted. Please go back and refresh the last page.')