import csv
import os.path
from csv import DictWriter
#se o csv não existir, cria ele
if os.path.exists('teste.csv')==False:
    with open('./teste.csv', 'w') as csvfile:
        write=csv.writer(csvfile, delimiter=';')
        write.writerow(['Titulo','Autor', 'Ano', 'Status','Emprestado para' ])
        write.writerow(['Como fazer sentido e bater o martelo','Alexandro Aolchique','2017','Disponivel',''])
        write.writerow(['Sejamos todos feministas','Chimamanda Ngozi Adichie','2015','Disponivel',''])
        write.writerow(['Basquete 101','Hortência Marcari','2010','Disponivel',''])
        csvfile.close()
csvfile = "teste.csv"
estante=dict()
def dados():
    file=open(csvfile,'r',encoding='utf-8')
    reader=csv.DictReader(file,delimiter=';')
    for indice,row in enumerate(reader):
        estante[indice+1]=row
    file.close()
def mostrarlivros():
    for valor in estante:
        livro=estante[valor]
        print(f"Numero: {valor}")
        print(f"Titulo: {livro['Titulo']}")
        print(f"Autor: {livro['Autor']}")
        print(f"Ano: {livro['Ano']}")
        print(f"Status: {livro['Status']}")
        if livro['Emprestado para']!='' or livro['Emprestado para']==None:
            print(f"Emprestado para: {livro['Emprestado para']}")
        print()
def gravardados():
    with open('./teste.csv','w', newline='\n') as csvfile:
        write=csv.writer(csvfile, delimiter=';')
        write.writerow(['Titulo','Autor', 'Ano', 'Status','Emprestado para'])
        headercsv=['Titulo','Autor', 'Ano', 'Status','Emprestado para' ]
        escrever=DictWriter(csvfile,fieldnames=headercsv,delimiter=';')
        for x in estante:
            escrever.writerow(estante[x])
        csvfile.close()
dados()
mostrarlivros()
controle=-1
print()
while controle!=0:
    controle: str=input("Digite 1 para PEGAR um livro\nDigite 2 para DEVOLVER um livro\nDigite 3 para DOAR um livro\nDigite 0 para sair\nQual opção? ")
    #verifica se digitou um número
    try:
        controle: int = int(controle)
    except Exception:
        controle=-1
    #pega o livro
    if controle==1:
        while True:
            dados()
            valor=int(input("Digite o Numero do livro ou 0 para sair: "))
            digitado=estante[valor]
            if digitado['Status']=='Disponivel':
                digitado['Status']='Indisponivel'
                digitado['Emprestado para']=input('Digite seu nome: ')
                print("Você pegou o livro emprestado!!!")
                gravardados()
                break
            elif digitado['Status']=='Indisponivel':
                print("Este livro já está emprestado!!!")
            elif valor==0:
                break
    #devolve o livro
    elif controle==2:
        while True:
            dados()
            valor=int(input("Digite o Numero do livro emprestado ou 0 para sair: "))
            digitado=estante[valor]
            if digitado['Status']=='Indisponivel':
                digitado['Status']='Disponivel'
                digitado['Emprestado para']=''
                print("Você devolveu o livro!!!")
                gravardados()
                break
            elif digitado['Status']=='Disponivel':
                print("Você não pegou este livro, devolva apenas livros que foram emprestados!!!")
            elif valor==0:
                break
    #doa o livro
    elif controle==3:
        headercsv=['Titulo','Autor', 'Ano', 'Status','Emprestado para' ]
        escreva=dict()
        escreva["Titulo"]=input("Digite o Título do livro: ")
        escreva["Autor"]=input("Digite o Autor do livro: ")
        escreva["Ano"]=input("Digite o Ano do livro: ")
        escreva["Status"]='Disponivel'
        escreva["Emprestado para"]=''
        with open('./teste.csv','a', newline='\n') as csvfile:
            escrever=DictWriter(csvfile,fieldnames=headercsv,delimiter=';')
            escrever.writerow(escreva)
            csvfile.close()
        file=open("./teste.csv",'r',encoding='utf-8')
        reader=csv.DictReader(file,delimiter=';')
        cont=0
        for row in reader:
            cont=cont+1
        file.close()
        print(f"\nNumero: {cont}")
        print(f"Titulo: {escreva['Titulo']}")
        print(f"Autor: {escreva['Autor']}")
        print(f"Ano: {escreva['Ano']}")
        print(f"Status: {escreva['Status']}")
        print("\nVocê doou o livro com sucesso\n")
    #finaliza
    elif controle!=0:
        print("\nValor inválido\n")