clientes=dict()
totalimposto=0
totalmercadoria=0
totalgeral=0
#checa se é as opções
def check_input(arg, opcoes):
    while arg not in opcoes:
         arg = input("Digite S para continuar e N para sair ").lower()
    return arg
id = 1
#pega os dados dos clientes
while True:
    dados=dict()
    dados["cliente"]=input("Nome do cliente: ")
    dados["quantidade"]=input("Digite a quantidade: ")
    clientes[id] = dados
    continuar = check_input(input("Digite S para continuar e N para sair ").lower(), ["s", "n"])
    if continuar=='n':
        break
    
    id += 1
#faz o processamento dos dados
for x in clientes:
    valor=clientes[x]
    valor["totalmercadoria"]=4.50*int(valor["quantidade"])
    valor["icms"]=(valor["totalmercadoria"]*18.0)/100
    valor["ipi"]=(valor["totalmercadoria"]*4.0)/100
    valor["pis"]=(valor["totalmercadoria"]*1.86)/100
    valor["cofins"]=(valor["totalmercadoria"]*8.54)/100
    valor["totalvenda"]=valor["totalmercadoria"]+valor["icms"]+valor["ipi"]+valor["pis"]+valor["cofins"]
    valor["totaltaxas"]=valor["icms"]+valor["ipi"]+valor["pis"]+valor["cofins"]
    totalimposto=totalimposto+valor["totaltaxas"]
    totalmercadoria=totalmercadoria+valor["totalmercadoria"]
    totalgeral=totalgeral+valor["totalvenda"]
#apresenta os valores
for x in clientes:
    valor=clientes[x]
    print("* "*10)
    print(f"Cliente: {valor['cliente']}")
    print(f"ICMS: {valor['icms']:.2f}")
    print(f"IPI: {valor['ipi']:.2f}")
    print(f"PIS: {valor['pis']:.2f}")
    print(f"COFINS: {valor['cofins']:.2f}")
    print(f"Total Venda: {valor['totalvenda']:.2f}")
print("* "*10)
print(f"Total Impostos: {totalimposto:.2f}")
print(f"Total Mercadorias: {totalmercadoria:.2f}")
print(f"Total Geral: {totalgeral:.2f}")