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
viewer.render


# for canvas in viewer: python é lento portanto é necessário filtrar resultados antes de ler e/ou exibir 
    #canvas_strings = canvas.strings #segura todos os caracteres de forma individual, sera importante.
    #adquire as strings por caractere individual, ver se ha como dividir por espaco.

    # for canvas in viewer:
    #    page_text = canvas.text_content
    #    print(page_text)


# começando implementacao de tabela hash para token separando por espaco ' '
# metodo = adquirir caractere individual, atribui-lo a um vetor e acessar conteudo. (Procurando APIs de hash para utilizcao de codigo open source)
# usar hash table nativa com 'hash_table = {}'



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
            
        else:
            teste = hash_table.get(char)
            
            if teste:
                hash_table[char] += 1
            else:
                hash_table[char] = 1

            char = ''

resultados = sorted(hash_table.items(), key=operator.itemgetter(1))

print(resultados)

