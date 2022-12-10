import os
from constants import *
import psycopg2

def connection_postgre_(con_postgre_db):
    """Define a Conexao com o postgre
       Para extrair os csv's"""
    cur = con_postgre_db.cursor()
    print('Conexao estabelecida!!')
    return cur


def sql(_tabelas):
    """Faz as querys que gerarão as tabelas
       E formata elas para que sejam transformadas em csv's"""
    query = f""" SELECT * FROM public.{_tabelas} """
    output = "COPY ({0}) TO STDOUT WITH CSV HEADER ".format(query)
    return output


def create_dir(_tabelas,_date,con_postgre_db,path_dir_postgre):
    """Função que gerará os diretórios de acordo com a data para cada tabela do postgre
       que está no modulo de constantes. Além disso, cria um csv para cada diretorio baseado na data """
    try:
        
        directory = f'{path_dir_postgre}/{_tabelas}/' + _date
        if not os.path.exists(directory):
            os.makedirs(directory)
        print('Diretorios Criados')
        
        with open(f"{directory}/{_tabelas}.csv","w",encoding='utf-8') as file:
            connection_postgre_(con_postgre_db).copy_expert(sql(_tabelas), file)
            print(f'Criando o CSV {_tabelas}\n CSV Criado!')

            connection_postgre_(con_postgre_db).close()
    
    except Exception as erro:
        print(f'falha na geração do CSV {erro}')


def create_csv(_date,con_postgre_db,path_dir_postgre):
    # Exportando os csv's do Postgre para os respectivos locais a partir da constante LISTA_TABELAS
    for name in LISTA_TABELAS:
        try:
            if name != 'order_details':   
                create_dir(
                            _tabelas=f'{name}',
                           _date=_date,
                           con_postgre_db=con_postgre_db,
                           path_dir_postgre=path_dir_postgre
                          )
        
        except:
            pass
        