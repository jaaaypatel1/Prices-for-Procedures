from django.shortcuts import render
from .models import Item

def search_view(request):
    query = request.GET.get('q', '')
    results = Item.objects.filter(name__icontains=query) if query else []
    return render(request, 'search/search.html', {'query': query, 'results': results})
