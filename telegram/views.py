from django.shortcuts import render
from .forms import MyForm

def order_view(request):
    form = MyForm()
    return render(request, 'telegram/order.html', {'form': form})
