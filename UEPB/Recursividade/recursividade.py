################  Exemplos  ####################

# Recursividade Direta
#  - Torre de Hanoi
def hanoi(disco, origem = "A", destino = "B", auxiliar = "C"):
    if (disco <= 0):
        return
    
    hanoi(disco - 1, origem, auxiliar, destino)
    
    print(f'Movendo disco {disco} de {origem} para {auxiliar}')
    
    hanoi(disco - 1, destino, origem, auxiliar)

# - Recursive Function
def recusrsiveFunction(x):
    if (x <= 4):
        print(x)
        recusrsiveFunction(x + 1)

# Recursividade Indireta - 
# - Fatorial
def fatorial1(x):
    if (x <= 1):
        return x
    else:
        return (x * fatorial2(x))


def fatorial2(x):
    return fatorial1(x-1)

################  Recursividade  ####################

def listarFuncoes():
    listaDeFuncoes = database()

    for i in range(len(listaDeFuncoes)):
        print([f"{listaDeFuncoes[i]['Índice']}", listaDeFuncoes[i]["Título"]])

    print()
    num = int(input(f"- Digite o numero da funçao que deseja executar: "))
    print()

    executarFuncao(listaDeFuncoes, num)


def database():
    listaDeFuncoes = [
        {"Índice": 1, "Título": "Torre de Hanoi", "Função": hanoi, "Input": "--> Informe quantos discos a torre terá: "},
        {"Índice": 2, "Título": "Recursividade Function", "Função": recusrsiveFunction, "Input": "--> Digite 0 para iniciar: "},
        {"Índice": 3, "Título": "Fatorial", "Função": fatorial1, "Input": "--> Informe qual número deseja calcular o fatorial: "}
    ]
    
    return listaDeFuncoes


def executarFuncao(listaDeFuncoes, num):
    if(num == 3) :
        print(listaDeFuncoes[num-1]["Função"](int(input(listaDeFuncoes[num-1]["Input"]))))
    else :
        listaDeFuncoes[num-1]["Função"](int(input(listaDeFuncoes[num-1]["Input"])))
    
    print()
    loop = input("Deseja realizar outra função? ")
    print()
    if loop == "sim":
        listarFuncoes()
        

################  Iniciar  ####################

listarFuncoes()