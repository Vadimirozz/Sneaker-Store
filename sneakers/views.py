from django.shortcuts import render
from .models import Sneakers
from django.views.generic import DetailView


def sneakers(request):
	sneakers = Sneakers.objects.all()
	return render(request, 'main/layout.html', {'sneakers': sneakers})

class SneakersDetailView(DetailView):
	model = Sneakers
	template_name = 'main/details_view.html'
	context_object_name = 'sneaker'

def your_view(request):
    search_query = request.GET.get('message', '')  # Получаем значение из поисковой строки
    sneakers = Sneaker.objects.filter(name__icontains=search_query)  # Фильтрация кроссовок по введенному запросу
    return render(request, 'your_template.html', {'sneakers': sneakers, 'search_query': search_query})





