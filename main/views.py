from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'npm': 2206826476,
        'kelas': 'PBP-A',
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, "main.html", context)

def lightcones(request):
    items = Item.objects.filter(user=request.user).order_by('-rarity', 'name')
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

@csrf_exempt
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

@csrf_exempt
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
    if request.method == 'GET':
        try:
            item = Item.objects.filter(user=request.user).get(pk=item_id)
        except Item.DoesNotExist:
            return JsonResponse({'message': 'Item not found'}, status=404)

        updated_amount = request.GET.get('amount', None)
        if updated_amount is not None:
            item.amount = updated_amount
            item.save()
            return JsonResponse({'message': 'The amount has been increased by 1'})
        else:
            return JsonResponse({'message': 'No data provided'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

def decrease_amount(request, item_id):
    if request.method == 'GET':
        try:
            item = Item.objects.filter(user=request.user).get(pk=item_id)
        except Item.DoesNotExist:
            return JsonResponse({'message': 'Item not found'}, status=404)

        updated_amount = request.GET.get('amount', None)
        if updated_amount is not None:
            item.amount = updated_amount
            item.save()
            return JsonResponse({'message': 'The amount has been decreased by 1'})
        else:
            return JsonResponse({'message': 'No data provided'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'DELETE':
        try:
            item = Item.objects.filter(user=request.user).get(pk=item_id)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully'})
        except Item.DoesNotExist:
            return JsonResponse({'message': 'Item not found'}, status=404)

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user).order_by('-rarity', 'name')
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        rarity = request.POST.get("rarity")
        lc_path = request.POST.get("lc_path")
        base_atk = request.POST.get("base_atk")
        base_hp = request.POST.get("base_hp")
        base_def = request.POST.get("base_def")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, rarity=rarity, 
                           lc_path=lc_path, base_atk=base_atk, base_hp=base_hp, base_def=base_def, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"],
            rarity = int(data["rarity"]),
            lc_path = data["lc_path"],
            base_atk = int(data["base_atk"]),
            base_hp = int(data["base_hp"]),
            base_def = int(data["base_def"])
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def show_json_by_user(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")