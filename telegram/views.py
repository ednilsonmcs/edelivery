from django.shortcuts import render
from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Manipule os dados do formulário aqui e faça a requisição à API, se necessário
            print('>')
        else:
            # O formulário não é válido, você pode lidar com isso aqui
            print('>')
    else:
        form = MyForm()
    return render(request, 'telegram/my_form.html', {'form': form})
