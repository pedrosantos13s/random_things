from random import randrange

def aula_stats(n, x):
    i = 0
    lista = []
    
    while i < n:
        lista.append(randrange(0, x))
        i += 1
    
    media = sum(lista) / n
    
    lista.sort()
    meio = n // 2

    if (n % 2 == 0):
        mediana = sum(lista[meio-1 : meio + 1]) / 2
    else:
        mediana = lista[meio]
    
    return (media, mediana)