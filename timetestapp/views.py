from django.shortcuts import redirect, render
from .models import Customer
from .forms import CutomerForm

# Create your views here.
def users(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request, 'customers.html', context)

def user(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer':customer}
    return render(request, 'customer.html', context)

def addUser(request):
    form = CutomerForm()
    if request.method == "POST":
        form = CutomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(users)
    context = {'form': form}
    return render(request, 'add-customer.html', context)

def updateUser(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CutomerForm(instance=customer)
    if request.method == "POST":
        form = CutomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect(users)
    context = {'form': form}
    return render(request, 'add-customer.html', context)
 
def deleteUser(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect(users)
    context = {"customer":customer}
    return render(request, 'delete.html', context)