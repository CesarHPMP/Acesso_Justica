import operator
from django.shortcuts import render
from pdfreader import SimplePDFViewer

def home(request):
    return render(request, 'parseapp/search.html')

def parse_pdf(request):
    keyword = request.GET.get('keyword', '').lower()

    fd = open("./DATA/Constituicao.ADCTde1988EC132.pdf", "rb")
    viewer = SimplePDFViewer(fd)

    texto = ''
    resultados = set()
    canvas_strings = ''
    hash_table = {}
    holder = []
    characters = ''

    # Read and concatenate text from the PDF
    for canvas in viewer:
        if canvas_strings:
            canvas_strings += canvas.strings
        else:
            canvas_strings = canvas.strings

    print(canvas_strings)

    # Split the text into articles and create the hash table
    for index, values in enumerate(canvas_strings):
        holder = values.split("Art.")
        characters = values.split(" ", "")
        print(characters)
        
        if texto:
            texto += holder
        else:
            texto = holder
            # Store articles in the hash table
    for split in texto:
        words = split.lower().split()  # Split the text into individual words
        for word in words:
            if word not in hash_table:
                hash_table[word] = []
            hash_table[word].append(split)

    # Find results that match the keyword
    if keyword in hash_table:
        for entry in hash_table[keyword]:
            resultados.add(entry)

    context = {
        'resultados': list(resultados),
        'keyword': keyword
    }
    return render(request, 'parseapp/results.html', context)
