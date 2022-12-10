import psycopg2
import mysql.connector as mysql
import time
from constants import *
from from_postgre import *
from mysql_environment import *
from treatments import *


def main():

# Variables that could change before the process:
    con_postgre_db = psycopg2.connect(dbname='indicium_postgre', user='postgre', host='localhost', password='postgre',port='5092')
    con_mysql = mysql.connect(host='localhost', user='root',password='mysql',port='5091')          
    _date = time.strftime("%d-%m-%y")
    path_dir_postgre = '../csv_transport/dados/pastas_postgre_csv_files'
    path_csv_external_files = '../csv_transport/dados/csv_files'
    path_final_result = '../csv_transport/dados/the_goal'
    db_name = 'indicium_challenge'
    
    
# Iniciating the Postgre environ on local machine
    connection_postgre_(con_postgre_db=con_postgre_db)
    
# Exporting of csv's for the Postgre directorys, directorys responsible for the daily storage.
    create_csv(
               _date=_date,
               con_postgre_db=con_postgre_db,
               path_dir_postgre=path_dir_postgre
              )
    
#Treatments to MySQL accepts the data  
    try:
        treat_nan(
                  _date=_date,
                  path_dir_postgre=path_dir_postgre,
                  path_csv_external_files=path_csv_external_files
                 )
        treat_specific(_date=_date,path_dir_postgre=path_dir_postgre) 
    
    except Exception as e:
        print(f'Erro na correção dos dados: {e}')
        
# Creating the MySQL Environ.
    try:
        create_mysql_db(con_mysql=con_mysql,db_name=db_name)
        # Variable that after the SGBD connection.
        con_mysql_db = mysql.connect(host='localhost', database=db_name, user='root', password='mysql',port='5091')
        drop_tables(con_mysql_db=con_mysql_db)
        create_tables(con_mysql_db=con_mysql_db)     
         
        insert_mysql(
                     con_mysql_db=con_mysql_db,
                     _date=_date,
                     path_dir_postgre=path_dir_postgre,
                     path_csv_external_files=path_csv_external_files
                    )
    
# Finishing the Challenge.
        the_goal(con_mysql_db=con_mysql_db,path_final_result=path_final_result)
    
    except Exception as e:
        print(f'Falha ao gerar os dados: {e}')
        
    

if __name__=='__main__':
    main()  

