from django.shortcuts import render, redirect
from coffee_shop.models import Bakery
from coffee_shop.forms import BakeryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'home_text': "welcome to home page"
    }
    return render(request, 'home.html', context)


@login_required
def cake(request):
    context = {
        'cake_text': "Click on your favourite cake to order now!!!!"
    }
    return render(request, 'cake.html', context)


@login_required
def pricing(request):
    if request.method == 'POST':
        form = BakeryForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
        messages.success(request, "Your order placed")
        return redirect('order')
    else:
        all_quantity = Bakery.objects.all
        return render(request, 'pricing.html', {'all_quantity': all_quantity})


@login_required
def order(request):
    all_quantity = Bakery.objects.filter(manager=request.user)
    return render(request, 'order.html', {'all_quantity': all_quantity})


def contact(request):
    context = {
        'contact_text': "Call on the given number to contact us!"
    }
    return render(request, 'contact.html', context)
