
def h_index_linear(citacoes):
    n = len(citacoes)
    
    for i in range(n):
        h = i + 1
        if citacoes[i] < h:
            return i
    
    return n


def h_index_binaria(citacoes):
    n = len(citacoes)
    esq = 0
    dir = n - 1
    resultado = 0
    
    while esq <= dir:
        meio = (esq + dir) // 2
        h = meio + 1
        
        if citacoes[meio] >= h:
            resultado = h
            esq = meio + 1
        else:
            dir = meio - 1
    
    return resultado


cit1 = [6, 5, 3, 1, 0]
print("Citacoes:", cit1)
print("Linear:", h_index_linear(cit1))
print("Binaria:", h_index_binaria(cit1))

print()

cit2 = [3, 1, 1]
print("Citacoes:", cit2)
print("Linear:", h_index_linear(cit2))
print("Binaria:", h_index_binaria(cit2))

print()

cit3 = [100, 100, 100]
print("Citacoes:", cit3)
print("Linear:", h_index_linear(cit3))
print("Binaria:", h_index_binaria(cit3))

print()

cit4 = [10, 8, 5, 4, 3]
print("Citacoes:", cit4)
print("Linear:", h_index_linear(cit4))
print("Binaria:", h_index_binaria(cit4))