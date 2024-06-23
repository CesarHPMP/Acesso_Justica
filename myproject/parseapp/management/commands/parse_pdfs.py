import os
from django.core.management.base import BaseCommand
from pdfreader import SimplePDFViewer
from parseapp.models import Article

class Command(BaseCommand):
    help = 'Parse all PDFs in ./DATA and store articles in the database'

    def handle(self, *args, **options):
        data_dir = './DATA'
        for filename in os.listdir(data_dir):
            if filename.endswith(".pdf"):
                filepath = os.path.join(data_dir, filename)
                self.parse_pdf(filepath)

    def parse_pdf(self, filepath):
        with open(filepath, "rb") as fd:
            viewer = SimplePDFViewer(fd)
            canvas_strings = ''
            
            for canvas in viewer:
                if canvas_strings:
                    canvas_strings += canvas.strings
                else:
                    canvas_strings = canvas.strings

            texto = ''.join(canvas_strings)
            articles = texto.split('Art.')
            
            for article in articles:
                if article.strip():  # Skip empty strings
                    title = article.split('.')[0].strip()
                    content = article.strip()
                    Article.objects.create(title=title, content=content)
                    self.stdout.write(self.style.SUCCESS(f'Successfully parsed article: {title}'))

