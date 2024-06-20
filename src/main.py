
with open('leis.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

lei = texto.split("Art.")

keyword = input("Informe a palavra chave que deseja buscar: ")

for leis in lei:
    if keyword in leis:
        print("\n----------------------------------------------------------------------")
        print(leis)
        print("----------------------------------------------------------------------\n")
    