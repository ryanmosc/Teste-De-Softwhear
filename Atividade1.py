import random
lista = [random.randint(1, 100)for _ in range(5)]



def adicionar_numero(lista):
    numero = input("Qual numero deseja adicionar?")
    lista.append(numero)
    return (lista)

def remover_numero(lista):
    print(lista)
    numero_retirar = input("Qual deseja retirar?")
    lista.remove(numero_retirar)
    return (lista)
    
def mostrar_lista(lista):
    print("{lista}")
    
def somar (lista):
    for numero in lista:
        soma=soma+numero

def media_lista (lista):
    return sum(lista)/len(lista)


while True:
    print("Escolha uma dentre essas 6 funções para proseguir")
    print("1-Adicionar numero a lista")
    print("2-Retirar um numero da lista")
    print("3-Mostrar a lista")
    print("4-Calcular a soma da lista")
    print("5-Calcular a média")
    op = input("Qual operação deseja chamar?")
    
    if op == '1':
        print(adicionar_numero(lista))

    if op == '2':
        print(remover_numero(lista))
    break


        
