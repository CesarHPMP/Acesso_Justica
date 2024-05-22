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


fd = open("../DATA/Constituicao.ADCTde1988EC132.pdf", "rb")
viewer = SimplePDFViewer(fd)

hash_table = {}
texto = []
char = ''
resultados = []

for canvas in viewer:
    canvas_strings = canvas.strings
    texto = canvas_strings
    for x in texto:

        if x != ' ' and x != ',' and x != ';' and x != '?' and x != '!' and x != '.':
            char += x;
            
        elif char != '':
            teste = hash_table.get(char)
            
            if teste:
                hash_table[char] += 1
            else:
                hash_table[char] = 1

            char = ''

resultados = sorted(hash_table.items(), key=operator.itemgetter(1))

print(resultados)

