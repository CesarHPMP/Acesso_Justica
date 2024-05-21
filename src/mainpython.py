# main para parseador em python, passos seguem:

#import ou criar tabela hash para maior velocidade de processsamento e para filtragem baseada em frequencia 
#em que os tokens aparecem 

#problemas a serem resolvidos: 
# - Hash apenas guarda os tokens e suas frequencias mas nao onde estao no arquivo(Talvez guardar em classe como metodo ou dado ex: token.posicoes(token))
# - Guardar local em que dado se encontra dentro do arquivo e retornanr para usuario como resultado de pesquisa.
# - avaliacao correta de importancia para melhores resultados (frequencia do token em um dado arquivo e ou quao perto do inicio este aparece?)

import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

fd = open("../DATA/Constituicao.ADCTde1988EC132.pdf", "rb")
viewer = SimplePDFViewer(fd)

print(viewer.metadata)

for canvas in viewer:
    canvas_strings = canvas.strings
    # print(canvas_strings) adquire as strings por caractere individual, ver se ha como dividir por espaco.

for canvas in viewer:
    page_text = canvas.text_content
    print(page_text)
