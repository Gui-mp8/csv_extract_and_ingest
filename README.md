<h1>Indicium Challenge</h1>

<h2>About:</h2 >

<p>
The goal of this challenge is to take data from two different types of data sources (PostgreSQL and local), transfer these data to a SGBD of my choice(MySQL) and then generate a .csv file from a query that returns the combination of the table orders and the table order_details.
</p>

#

<h2>Previous Information</h2 >
<p></p>
<h3>Let's talk about the Host:</h3>

<p>

- The host for all connections will be (localhost or 0.0.0.0 or 127.0.0.1), these 3 are the same thing 
</p>

<h3>Let's talk about the Ports:</h3>

<p>

- The Ports will be used to connect the Python Program to the docker databases. To see the ports that are open, you can check these links: 
  - Windows: https://www.alphr.com/how-to-check-which-ports-open-windows-10-pc/
  - Linux: https://adamtheautomator.com/check-if-a-port-is-open-in-linux/
  - Mac: https://apple.stackexchange.com/questions/117644/how-can-i-list-my-open-network-ports-with-netstat
</p>

#
<h2>Tecnologies:</h2>

  <table>
    <tr>
      <td>Docker</td>
      <td>Python</td>
      <td>DBeaver(Optional)</td>
    </tr>
      <tr>
      <td>2 containers</td>
      <td>3.10</td>
      <td>PostgreSQL, MySQL</td>
    </tr>
  </table>

<h3>The docker containers served to use Postgre and MySQL, one SGBD for each container.</h3>

#

<h2>Prerequisites:</h2>
<p>

- Python 
  - It's necessary a version between 3.7 - 3.10, you can check the versions in this link : https://www.python.org/downloads/ or if you already has python, you can check the version passing this code

  ```
  python -V
  ```

- Docker
  - You can download on this link: https://www.docker.com

- Dbeaver(Optional)
  - You can download on this link: https://dbeaver.io/download/

<h3> 

**OBS** : DBeaver is optional because it can be use to see the data that your're managing</h3>

</p>

#

<h2>Making the SGBD's Environment:</h2>
<p>
  <h3>
  For the creation of the databases environment, it's only necessary to run the docker-compose.yaml.
<p>

  **OBS: Before you run the docker-compose.yaml, pay attention at the nowthwind.sql path on volumes. If you don't set it correctly, you'll not succeed in runing the code.**

```
[your_path]\desafio_indicium\northwind.sql:/docker-entrypoint-initdb.d/northwind.sql
```
Exemple:

```
C:\Users\gui_p\vscode\python\desafio_indicium\northwind.sql:/docker-entrypoint-initdb.d/northwind.sql
```
  </h3>
</p>
<h3>1 - Creating PostgreSQL and MySQL in docker:</h3>

```
docker-compose up -d
```
<p>

This command will create the 2 containers that we'll be using
</p>

<p><h3>Some Important Info:</h3>

  <p>
  
  - **MYSQL_ROOT_PASSWORD** = It's the password that says: ' You can do anything in here'.<br>

  <p>

  - **POSTGRES_USER** = It's the root user in Postgre.<br>
  <p>

  - **POSTGRES_PASSWORD** = It's the root password in Postgre.<br>
  <p>

  - **POSTGRES_DB** = It's the principal Database in your Postgre, it's necessary set this for the connection.<br>
  <p>

  - **Ports** = It's the gateway between your PC and the Container,5092:5432. The 5092 is the PC Port and 5432 is the SGBD Port, all the SGBD's has a default Port. Example : Postgre = 5432 and MySQL = 3306<br>
</p>

<h3>2 - Connecting to DBeaver(Optional):</h3>

<p>
  <h4>

  It's only necessary to pass the informations that you set in your docker-compose.yaml to connect with the SGBD's ,just follow this link: https://hevodata.com/learn/dbeaver-postgresql/
   
  </h4>

  <h3> 

  **OBS** : MySQL root user is **root** as default</h3>

</p>

#



<h2>Making the Python Environment:</h2>
<p>
<h3>1- Create the python environment in a project using the code bellow.</h3> 

```
python -m venv .venv
```
<h3>2 - Activate the project enviroment.</h3>

```
.venv/Scripts/Activate
```
<h3>3 - Install the Requiriments that are listed with the code below, or just see the code and install the libs.</h3>

```
pip install -r requirements.txt
```
</p>

#

<h2>Setting the main.py file</h2 >

<p>
  <h3>
  After setting all the enviroment's you can start the setting the main.py file.
  </h3>
</p> 

<p>
  <h3>
  Let's open the main.py and understand how it's works
  </h3>
</p> 

<p>
  <h3>
  Variables:</h3>
  <h4>

  - **con_postgre_db** = Here you must set the Postgre settings that you set previously. Remember what i've said about the host and ports 

  - **con_mysql** = Here you must set the MySQL settings that you set previously. Remember what i've said about the host and ports 

  - **_date** = Here you can choose the data that workflow will happen. If you choose days that passed, the data will be from these days

  - **path_dir_postgre** = Here you can choose the path wich you Postgre directory will stay

  - **path_csv_external_files** = Here is the path that you choose to store your external csv files, like the orders_details.csv

  - **path_final_result** = Here is the path that you choose to receive the final result

  - **db_name** = Here is where you choose the name of the MySQL Database that'll store the data from Postgre 

  - **con_mysql_db** = Here you must set the MySQL settings that you set previously **AND the db_name** that you choose before. Remember what i've said about the host and ports 
  </h4>
</p> 

<p>
  <h3>
  Functions: 
  </h3>
  <h4>

  - **connection_postgre_** = Makes the connection with postgre

  - **create_csv** = Exports the .csv files for the Postgre directorys, directorys responsibles for the daily storage.

  - **treat_nan** = Treats the NaN values because MySQL don't accept NaN values.

  - **treat_specific** - Treats the NaN values like date NaN values. A column with date NaN can't receive a normal null value like 0, so, it was necessary transform this value in other thing like '1999-99-99' to say that is a null value that can enter in MySQL.

  - **create_mysql_db** - Creates a database in MySQL that will receive the csv's data.

  - **drop_tables** - Drops the tables to not duplicate the static data.

  - **create_tables** - Recreates the tables droped to receive the static data without duplication.

  - **insert_mysql** - Inserts the respective data into their respective tables.

  - **the_goal** - Generate the goal of the challenge.
  </h4>
</p> 

#

<h2>Running main.py</h2 >

<p>
  <h3>
  After setting all the enviroment's and the variables, you can just run this command and enjoy the magic.

  ```
  python main.py
  ```
  </h3>
</p> 

#

<h2>Workflow</h2>

![workflow](https://user-images.githubusercontent.com/94998733/206047413-d4e16805-82e7-4cfe-9b45-45611d700a5b.PNG)


<p>
<h4>Step 1.1 - Python creates a connection with postgre.</h4>

<h4>Step 1.2 - Python creates the diretories separeted by the name of the tables and by day.</h4>

<h4>

Step 1.3 - Python creates the csv's in they respective diretories based on **the northwind.sql tables** and the day that the code is running.
</h4>

<h4>Step 2 - Python treats the NaN values. This must happen cause MySQL don't accept insert NaN values</h4>

<h4>Step 3.1 - Python creates a connection with MySQL.</h4>

<h4>Step 3.2 - Python creates a database in MySQL.</h4>

<h4>Step 3.3 - Python creates the tables in that database.</h4>

<h4>Step 3.4 - Python inserts the csv's data into their respective tables in the database.</h4>

<h4>Step 3.5 - Python generate the goal, which is a .csv file from a query that returns the combination of the tables orders and order_details.</h4>
</p>



