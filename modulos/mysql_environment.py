import time
import os
import csv

import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

from constants import *


def create_mysql_db(con_mysql, db_name):
    '''Function that connects python with MySQL'''
    try:

        if con_mysql.is_connected():

            print('Conectado ao MYSQL')
            cursor = con_mysql.cursor()
            cursor.execute(f"CREATE DATABASE {db_name}")
            print("Banco de Dados criado")

        else:
            print('O Banco de Dados já está criado')

    except Error as e:
        print("Erro ao se conectar com o Banco de Dados", e)

    time.sleep(0.1)


def drop_tables(con_mysql_db):
    '''Function that drops the existing tables '''
    try:

        if con_mysql_db.is_connected():

            cursor = con_mysql_db.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("\nVocê se conectou ao banco de dados: ", record)

            for tabela in LISTA_TABELAS:
                cursor.execute(f'DROP TABLE IF EXISTS {tabela};')
                print(f'\nA tabela {tabela} foi deletada')
                time.sleep(0.1)

    except Error as erro:
        print(f'\nErro ao dropar alguma tabela: {erro}')

        time.sleep(0.1)


def create_tables(con_mysql_db):
    '''Funçtion that creates empty tables to be filled'''
    try:
        print('Criando tabelas....')
    # in the below line please pass the create table statement which you want #to create
        cursor = con_mysql_db.cursor()
        for table in LISTA_DDL:
            cursor.execute(table)
            print(f' A tabela {table} foi criada')
            time.sleep(0.1)
        print("As tabelas foram criadas....")

    except Error as erro:
        print("Erro ao se conectar no MySQL", erro)


def insert_mysql(con_mysql_db, _date, path_dir_postgre, path_csv_external_files):
    '''Function that insert data into the new created tables'''

    try:

        cursor = con_mysql_db.cursor()

        for tabela in LISTA_TABELAS:
            if tabela != 'order_details':
                df = pd.read_csv(rf'{path_dir_postgre}/{tabela}/{_date}/{tabela}.csv',
                                 index_col=False, delimiter=',', encoding='utf8')

                print(f'\nDataframe {tabela} carregado')

                columns = df.shape[1]
                x = (',%s') * columns
                y = x.replace(',', '', 1)

                print('Automação de colunas realizado')

            # loop through the data frame
                for i, row in df.iterrows():
                    print(f'\nInserindo Dados: \n{tuple(row)}')
                # here %S means string values
                    # If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query
                    query = f"INSERT INTO indicium_challenge.{tabela} VALUES ({y})"
                    cursor.execute(query, tuple(row))
                    time.sleep(0.05)
                    print("Dados Inseridos:")
                # the connection is not auto committed by default, so we must commit to save our changes
                    con_mysql_db.commit()

            else:
                df = pd.read_csv(rf'{path_csv_external_files}/{tabela}.csv',
                                 index_col=False, delimiter=',', encoding='utf8')
                print(f'\nDataframe {tabela} carregado')

                columns = df.shape[1]
                x = (',%s') * columns
                y = x.replace(',', '', 1)

                print('Automação de colunas realizado')

            # loop through the data frame
                for i, row in df.iterrows():
                    print(
                        f'Inserindo Dados na tabela {tabela}:,\n{tuple(row)}')
                # here %S means string values
                    # If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query
                    query = f"INSERT INTO indicium_challenge.{tabela} VALUES ({y})"
                    cursor.execute(query, tuple(row))
                    time.sleep(0.1)
                    print("Dados Inseridos")
                # the connection is not auto committed by default, so we must commit to save our changes
                    con_mysql_db.commit()

    except Exception as e:
        print(f'Erro: {e}')
        pass


def the_goal(con_mysql_db, path_final_result):
    '''Query that gives the goal of the challenge'''
    try:
        cursor = con_mysql_db.cursor()
        query = '''SELECT 
                        b.product_id,
                        b.unit_price,
                        b.quantity,
                        b.discount,
                        a.* 
                FROM indicium_challenge.orders a
                LEFT JOIN indicium_challenge.order_details b
                ON a.order_id = b.order_id;'''

        cursor.execute(query)
        result = cursor.fetchall()

        directory = f'{path_final_result}'
        if not os.path.exists(directory):
            os.makedirs(directory)
        print('Diretorio Criado')

        file = csv.writer(
            open(f'{directory}/final_result.csv', 'w', encoding='utf-8'))
        for i in result:
            file.writerow(i)

        print('\nArquivo final salvo')

        print('\nCongratulations!!! \nYou Completed the Project!!!!!!')

    except Exception as e:
        print(f'Query Error, try to fix it \n {e}')
