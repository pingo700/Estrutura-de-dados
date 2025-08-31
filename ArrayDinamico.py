# Classe de representação de um Array dinâmico - K.B
# A ideia principal por dentro do array dinâmico é utilizar da estrutura fixa do array estático
# para redimensionar e aumentar o tamanho do "array" primário, desta forma despreucupando-se de
# estourar o tamanho da estrutura, assim podendo adicionar elementos dinâmicamente na memória e
# aproveitar os acessos de posições que a estrutura do array fornece.
# Link que usei: https://youtu.be/_dvxrMwzyX0
class DynamicIntArray:

    #Construtor da classe dinâmica
    def __init__(self, capacity=2):
        # Verifica a capacidade do array, ele precisa ser maior ou igual a zero
        # Observação:
        #    - Capacidade = Posição
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity        # Tamanho real do array interno
        self.size = 0                   # Quantos elementos o usuário colocou
        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)

    # Método para verificar se o array está vazio ou não.
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.capacity == self.size
    
    # Método para retornar o valor desejado na posição indicada
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora dos limites.")
        return self.data[index]

    # Método para atribuir valor a "posição" desejada dentro do array
    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora dos limites.")
        self.data[index] = value

    def append(self, value):
        # Verifico se o array já está cheio
        print(self.is_full())
        if self.is_full():
           self._resize(self.capacity * 2)
           self.data[self.size] = value
           self.size = self.size + 1
        else:
            self.data[self.size] = value
            self.size = self.size + 1

    def _resize(self, new_capacity):
        if new_capacity > self.capacity:
            print(f"⏫ Redimensionando de {self.capacity} para {new_capacity}")
        else:
            print(f"⏬ Redimensionando de {self.capacity} para {new_capacity}")

        # Cria um novo array estático para fazer a dinamicidade
        new_data = [0] * new_capacity

        # Vou copiar o array antigo(menor) para o array atual(maior)
        for i in range(self.size):
            new_data[i] = self.data[i]

        # Vou atualizar o atributo que armazena o array dinâmicamente na classe com o novo array
        self.data = new_data

        # Vou atualizar o tamanho da capacidade agora
        self.capacity = new_capacity


    # Não entendi a usabilidade desse método aqui :(
    def __str__(self):
        return str(self.data[:self.size])


lista = DynamicIntArray()

# Saída: Lista vazia!
if lista.is_empty():
    print("Lista vazia!")
else:
    print("Lista tem elementos.")

print("Adicionando o 10;")
lista.append(10)
#Saída: Lista:  [10] 
print("Lista: ", lista) 
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()

print("Adicionando o 20;")
lista.append(20)
#Saída: Lista:  [10, 20] 
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()

print("Adicionando o 30;")
lista.append(30)
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()


print("Adicionando o 40;")
lista.append(40)
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()

print("Adicionando o 50;")
lista.append(50)
# Saída: [10, 20, 30, 40, 50]   
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()        

