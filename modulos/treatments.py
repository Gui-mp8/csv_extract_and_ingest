import pandas as pd
import time
from constants import *

def treat_nan(_date,path_dir_postgre,path_csv_external_files):
    '''Função utilizada para tratar os valores vazios'''
    try:
        
        #data = time.strftime("%d-%m-%y")
        
        for tabela in LISTA_TABELAS:
            if tabela != 'order_details':
                df = pd.read_csv(rf'{path_dir_postgre}/{tabela}/{_date}/{tabela}.csv',
                                 index_col=False,delimiter=',',encoding = 'utf8')
                
                print(f'\nDataframe {tabela} Carregado')
                
                df1=df.fillna(0)
                print('Vazios Corrigidos!')

                df1.to_csv(f'{path_dir_postgre}/{tabela}/{_date}/{tabela}.csv',index=False,encoding='utf8')
                print('Csv Substituido')
                
            else:
                df = pd.read_csv(rf'{path_csv_external_files}/{tabela}.csv',
                                 index_col=False,delimiter=',',encoding = 'utf8')
                
                print(f'\nDataframe {tabela} Carregado')
                
                df1=df.fillna(0)
                print('Vazios Corrigidos!')

                df1.to_csv(f'{path_csv_external_files}/{tabela}.csv',index=False,encoding='utf8')
                print('Csv Substituido')
    
    except Exception as e:
        print(f'Falha ao carregar ou tratar dataframe {tabela}: {e}')
        

def treat_specific(_date,path_dir_postgre):
    '''Função utilizada para tratar valores especificos'''
    #data = time.strftime("%d-%m-%y")
    
    try:
        for tabela in LISTA_TABELAS:
            if tabela =='orders':
                df = pd.read_csv(rf'{path_dir_postgre}/{tabela}/{_date}/{tabela}.csv',
                                 index_col=False,delimiter=',',encoding = 'utf8')
                
                print(f'\nDataframe {tabela} Carregado')
                
                df1=df
                df1['shipped_date'].replace('0','0001-01-01',inplace=True)
                
                df1.to_csv(f'{path_dir_postgre}/{tabela}/{_date}/{tabela}.csv',index=False,encoding='utf8')
                print('Csv Substituido')
    except Exception as e:
        print(f'Falha ao carregar ou tratar dataframe {tabela}: {e}')
