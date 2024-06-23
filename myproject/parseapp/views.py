from django.shortcuts import render
from parseapp.models import Article

def home(request):
    return render(request, 'parseapp/search.html')

def parse_pdf(request):
    keyword = request.GET.get('keyword', '').lower()
    resultados = Article.objects.filter(content__icontains=keyword)

    context = {
        'resultados': resultados,
        'keyword': keyword
    }
    return render(request, 'parseapp/results.html', context)
