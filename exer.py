#--------------------------------------------------
def contar_vogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador

#--------------------------------------------------
def substituir_letra(string, letra_original, letra_substituta):
    return string.replace(letra_original, letra_substituta)

#--------------------------------------------------
def contar_palavras(string):
    return len(string.split())

#--------------------------------------------------
def contar_ocorrencias_palavra(frase, palavra):
    return frase.split().count(palavra)


#--------------------------------------------------
def k_maiores(lista, k):
    return sorted(lista, reverse=True)[:k]

#--------------------------------------------------
def somar_matrizes(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

#--------------------------------------------------

def intersecao(lista1, lista2):
    return [valor for valor in lista1 if valor in lista2]
#--------------------------------------------------

import random

def embaralhar(lista):
    random.shuffle(lista)
    return lista

#--------------------------------------------------
def encontrar_par(lista, alvo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares

#--------------------------------------------------
def frequencia_palavra(texto, palavra):
    palavras = texto.split()
    return palavras.count(palavra)
#--------------------------------------------------

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
#--------------------------------------------------
def numeros_primos(lista):
    return [numero for numero in lista if eh_primo(numero)]

#--------------------------------------------------
def menor_string(lista):
    return min(lista, key=len)

#--------------------------------------------------
def ler_arquivo_texto(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()
#--------------------------------------------------
import csv

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        return list(leitor_csv)

#--------------------------------------------------
import json

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)
#--------------------------------------------------
import os

def consolidar_arquivos_texto(diretorio):
    consolidado = ''
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            with open(caminho_arquivo, 'r') as arquivo:
                consolidado += arquivo.read() + '\n'
    return consolidado
#--------------------------------------------------
import csv
from collections import defaultdict

def mes_com_mais_vendas(nome_arquivo):
    vendas_por_mes = defaultdict(int)
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            mes = linha['Mês']
            valor_venda = int(linha['Valor'])
            vendas_por_mes[mes] += valor_venda
    return max(vendas_por_mes, key=vendas_por_mes.get)

#--------------------------------------------------
def mes_com_menos_vendas(nome_arquivo):
    vendas_por_mes = defaultdict(int)
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            mes = linha['Mês']
            valor_venda = int(linha['Valor'])
            vendas_por_mes[mes] += valor_venda
    return min(vendas_por_mes, key=vendas_por_mes.get)

#--------------------------------------------------
def vendedor_com_mais_menos_vendas(nome_arquivo):
    vendas_por_vendedor = defaultdict(int)
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            vendedor = linha['Nome']
            valor_venda = float(linha['Valor'])
            vendas_por_vendedor[vendedor] += valor_venda
    
    vendedor_mais_vendeu = max(vendas_por_vendedor, key=vendas_por_vendedor.get)
    vendedor_menos_vendeu = min(vendas_por_vendedor, key=vendas_por_vendedor.get)
    
    return vendedor_mais_vendeu, vendedor_menos_vendeu


