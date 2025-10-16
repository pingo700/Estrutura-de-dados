def particiona(arr, inicio, fim):
    pivo = arr[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1


def quicksort(arr, inicio, fim):
    if inicio < fim:
        pivo_idx = particiona(arr, inicio, fim)
        quicksort(arr, inicio, pivo_idx - 1)
        quicksort(arr, pivo_idx + 1, fim)


# a) Busca Linear
def busca_linear_insercao(arr, alvo):
    for i in range(len(arr)):
        if arr[i] >= alvo:
            return i
    return len(arr)


def busca_binaria_insercao(arr, alvo):
    esq = 0
    dir = len(arr) - 1
    
    while esq <= dir:
        meio = (esq + dir) // 2
        
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    
    return esq


arr = [1, 3, 5, 6]
alvo = 5
print("Array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Ordenado:", arr)
print("Linear:", busca_linear_insercao(arr, alvo))
print("Binaria:", busca_binaria_insercao(arr, alvo))

print()

arr2 = [1, 3, 5, 6]
alvo2 = 2
print("Array:", arr2)
quicksort(arr2, 0, len(arr2) - 1)
print("Ordenado:", arr2)
print("Linear:", busca_linear_insercao(arr2, alvo2))
print("Binaria:", busca_binaria_insercao(arr2, alvo2))

print()

arr3 = [9, 3, 7, 1, 5]
alvo3 = 4
print("Array:", arr3)
quicksort(arr3, 0, len(arr3) - 1)
print("Ordenado:", arr3)
print("Linear:", busca_linear_insercao(arr3, alvo3))
print("Binaria:", busca_binaria_insercao(arr3, alvo3))