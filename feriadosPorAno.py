import requests
import json
#SOLICITANDO O ANO PARA O USUÁRIO
ano = input('Digite o ano que deseja ver os feriados: ')

#ARMAZENANDO O REQUEST DA API NUMA VARIÁVEL
response = requests.get(f'https://brasilapi.com.br/api/feriados/v1/{ano}')

#CONDIÇÃO, SE RETORNO FOR 200, FORMATA EM JSON E IMPRIME AS DATAS COM OS NOMES
if response.status_code == 200:
    dadosApi = response.json()

    for i in dadosApi:
        print('\nNOME: ',i['name'])
        print('DATA: ',i['date'],'\n')
        print('--------------------------------')

#SE NÃO, APRESENTA MENSAGEM DE ERRO
else:
    print("Erro na requisição. Código:", response.status_code)