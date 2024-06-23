import operator
from django.shortcuts import render
from django.http import HttpResponse
from pdfreader import SimplePDFViewer

def home(request):
    return render(request, 'parseapp/search.html')

def parse_pdf(request):
    keyword = request.GET.get('keyword', '').lower()

    fd = open("./DATA/Constituicao.ADCTde1988EC132.pdf", "rb")
    viewer = SimplePDFViewer(fd)

    texto = ''
    resultados = []
    canvas_strings = ''
    hash_table = {}

    for canvas in viewer:
        if canvas_strings:
            canvas_strings += canvas.strings
        else:
            canvas_strings = canvas.strings

    for index, values in enumerate(canvas_strings):
        holder = values.split("Art.")
        if texto:
            texto += holder
        else:
            texto = holder

        for split in holder:
            words = split.lower().split()
            for word in words:
                if word not in hash_table:
                    hash_table[word] = []
                hash_table[word].append((index, split))

    if keyword in hash_table:
        resultados = [entry[1] for entry in hash_table[keyword]]

    context = {
        'resultados': resultados,
        'keyword': keyword
    }
    return render(request, 'parseapp/results.html', context)
