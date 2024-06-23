# main para parseador em python, passos seguem:

#import ou criar tabela hash para maior velocidade de processsamento e para filtragem baseada em frequencia 
#em que os tokens aparecem 

#problemas a serem resolvidos: 
# - Hash apenas guarda os tokens e suas frequencias mas nao onde estao no arquivo(Talvez guardar em classe como metodo ou dado ex: token.posicoes(token))
# - Guardar local em que dado se encontra dentro do arquivo e retornanr para usuario como resultado de pesquisa.
# - avaliacao correta de importancia para melhores resultados (frequencia do token em um dado arquivo e ou quao perto do inicio este aparece?)

import operator
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer


fd = open("./DATA/Constituicao.ADCTde1988EC132.pdf", "rb") 
viewer = SimplePDFViewer(fd)

texto = ''
resultados = []
canvas_strings = ''

for canvas in viewer:
    if canvas_strings:
        canvas_strings = canvas_strings + canvas.strings
        
    else:
        canvas_strings = canvas.strings

for values in canvas_strings:
    if texto:
        holder = values.split("Art.")
        texto+=holder

    else:
        texto = values.split("Art.")

keyword = input("Digite a lei que deseja ou palavra chave: ")

for splits in texto:
    if keyword in splits:
        print(splits)