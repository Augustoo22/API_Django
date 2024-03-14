from django.shortcuts import render
from books.models import Books

def exibir_dados(request):
    # Consulta o último objeto Books inserido no banco de dados
    last_book = Books.objects.last()
    return render(request, 'exibir_dados.html', {'book': last_book})
