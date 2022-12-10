LISTA_TABELAS = ['categories',
                 'customer_customer_demo',
                 'customer_demographics',
                 'customers',
                 'employees',
                 'employee_territories',
                 'orders',
                 'products',
                 'region',
                 'shippers',
                 'suppliers',
                 'territories',
                 'us_states',
                 'order_details']


TABLE_CATEGORIES = '''CREATE TABLE categories (
                                                category_id smallint NOT NULL,
                                                category_name character varying(15) NOT NULL,
                                                description text,
                                                picture blob
                                               )'''
                                            
TABLE_CUSTOMER_CUSTOMER_DEMO = '''CREATE TABLE customer_customer_demo (
                                                                        customer_id varchar(5) NOT NULL,
                                                                        customer_type_id varchar(5) NOT NULL
                                                                       )'''
                                                                       
TABLE_CUSTOMER_DEMOGRAPHICS = '''CREATE TABLE customer_demographics (
                                                                    customer_type_id varchar(5) NOT NULL,
                                                                    customer_desc text
                                                                )'''
                                                                
TABLE_CUSTOMERS = '''CREATE TABLE customers (
                                            customer_id varchar(5) NOT NULL,
                                            company_name character varying(40) NOT NULL,
                                            contact_name character varying(30),
                                            contact_title character varying(30),
                                            address character varying(60),
                                            city character varying(15),
                                            region character varying(15),
                                            postal_code character varying(10),
                                            country character varying(15),
                                            phone character varying(24),
                                            fax character varying(24)
                                            )'''    
                                            
TABLE_EMPLOYEES = '''CREATE TABLE employees (
                                            employee_id smallint NOT NULL,
                                            last_name character varying(20) NOT NULL,
                                            first_name character varying(10) NOT NULL,
                                            title character varying(30),
                                            title_of_courtesy character varying(25),
                                            birth_date date,
                                            hire_date date,
                                            address character varying(60),
                                            city character varying(15),
                                            region character varying(15),
                                            postal_code character varying(10),
                                            country character varying(15),
                                            home_phone character varying(24),
                                            extension character varying(4),
                                            photo blob,
                                            notes text,
                                            reports_to smallint,
                                            photo_path character varying(255)
                                            )'''                   

TABLE_EMPLOYEE_TERRITORIES = '''CREATE TABLE employee_territories (
                                                                    employee_id smallint NOT NULL,
                                                                    territory_id character varying(20) NOT NULL
                                                                  )'''                                                                                     
                                                                                                                                    
TABLE_ORDERS = '''CREATE TABLE orders (
                                        order_id smallint NOT NULL,
                                        customer_id varchar(5) NOT NULL,
                                        employee_id smallint NOT NULL,
                                        order_date date,
                                        required_date date,
                                        shipped_date date,
                                        ship_via smallint,
                                        freight real,
                                        ship_name character varying(40),
                                        ship_address character varying(60),
                                        ship_city character varying(15),
                                        ship_region character varying(15),
                                        ship_postal_code character varying(10),
                                        ship_country character varying(15)
                                    )'''

TABLE_PRODUCTS = '''CREATE TABLE products (
                                            product_id smallint NOT NULL,
                                            product_name character varying(40) NOT NULL,
                                            supplier_id smallint,
                                            category_id smallint,
                                            quantity_per_unit character varying(20),
                                            unit_price real,
                                            units_in_stock smallint,
                                            units_on_order smallint,
                                            reorder_level smallint,
                                            discontinued integer NOT NULL
                                          )'''
                                          
TABLE_REGION = '''CREATE TABLE region (
                                        region_id smallint NOT NULL,
                                        region_description text
                                      )'''   
                                      
TABLE_SHIPPERS = '''CREATE TABLE shippers (
                                            shipper_id smallint NOT NULL,
                                            company_name character varying(40) NOT NULL,
                                            phone character varying(24)
                                          )'''    
                                          
TABLE_SUPPLIERS = '''CREATE TABLE suppliers (
                                            supplier_id smallint NOT NULL,
                                            company_name character varying(40) NOT NULL,
                                            contact_name character varying(30),
                                            contact_title character varying(30),
                                            address character varying(60),
                                            city character varying(15),
                                            region character varying(15),
                                            postal_code character varying(10),
                                            country character varying(15),
                                            phone character varying(24),
                                            fax character varying(24),
                                            homepage text
                                            )'''        
                                            
TABLE_TERRITORIES = '''CREATE TABLE territories (
                                                territory_id character varying(20) NOT NULL,
                                                territory_description text NOT NULL,
                                                region_id smallint NOT NULL
                                                )'''       
                                                
TABLE_US_STATES = '''CREATE TABLE us_states (
                                            state_id smallint NOT NULL,
                                            state_name character varying(100),
                                            state_abbr character varying(2),
                                            state_region character varying(50)
                                            )'''     
                                            
#NOVA TABELA

TABLE_ORDER_DETAILS = '''CREATE TABLE order_details (
                                                    order_id smallint NOT NULL,
                                                    product_id smallint NOT NULL,
                                                    unit_price real,
                                                    quantity smallint,
                                                    discount real
                                                    )'''          
                                                    
LISTA_DDL = [TABLE_CATEGORIES,
             TABLE_CUSTOMER_CUSTOMER_DEMO,
             TABLE_CUSTOMER_DEMOGRAPHICS,
             TABLE_CUSTOMERS,
             TABLE_EMPLOYEES,
             TABLE_EMPLOYEE_TERRITORIES,
             TABLE_ORDERS,
             TABLE_PRODUCTS,
             TABLE_REGION,
             TABLE_SHIPPERS,
             TABLE_SUPPLIERS,
             TABLE_TERRITORIES,
             TABLE_US_STATES,
             TABLE_ORDER_DETAILS]
                                                                                                                                                                         
                                                                                                                                                                                                                                                                                   