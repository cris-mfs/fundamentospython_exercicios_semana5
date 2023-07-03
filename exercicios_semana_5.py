import csv
import matplotlib.pyplot as plt

def ler_dados_csv(caminho_ficheiro):
    with open(caminho_ficheiro, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def calcular_total_vendas_por_produto(dados):
    total_vendas = {}
    for linha in dados:
        produto = linha["produto"]
        qtd_vendida = int(linha["quantidade_vendida"])
        if produto in total_vendas:
            total_vendas[produto] += qtd_vendida
        else:
            total_vendas[produto] = qtd_vendida
    return total_vendas


# Ler dados
dados = ler_dados_csv("AtividadePedagogica4_10793_02.csv")

# Calcula e agrupa os produtos por total de vendas
total_vendas = calcular_total_vendas_por_produto(dados)

# ----------- Ordenar por quantidade vendida ----------- #
# Método 1
total_vendas_ordenado_1 = dict(sorted(total_vendas.items(), key=lambda item: item[1]))

# Método 2
def ordenar_dicionario(total_vendas):
    numeros_lista = []
    for produto, qtd_vendida in total_vendas.items():
        numeros_lista.append(qtd_vendida)
    n = len(numeros_lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numeros_lista[j] > numeros_lista[j + 1]:
                temp = numeros_lista[j]
                numeros_lista[j] = numeros_lista[j + 1]
                numeros_lista[j + 1] = temp
    dicionario_ordenado = {}
    for numero in numeros_lista:
        for produto, qtd_vendida in total_vendas.items():
            if qtd_vendida == numero:
                dicionario_ordenado[produto] = qtd_vendida
    return dicionario_ordenado

total_vendas_ordenado_2 = ordenar_dicionario(total_vendas)

# ----------- Criar Gráfico ----------- #
# Função para converter entradas do dicionário em listas separadas
def dicionario_para_lista(dicionario):
    lista1 = []
    lista2 = []
    for item1, item2 in dicionario.items():
        lista1.append(item1)
        lista2.append(item2)
    return lista1, lista2

eixo_x, eixo_y = dicionario_para_lista(total_vendas_ordenado_2)

plt.bar(eixo_x, eixo_y, color=['maroon', 'orange'])
plt.title('Vendas\n')
plt.ylabel('Vendas [un]')
plt.show()