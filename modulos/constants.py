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
                                        ship_country character varying(15),
                                        PRIMARY KEY (order_id)
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
                                                    discount real,
                                                    FOREIGN KEY (order_id) REFERENCES orders(order_id)
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
                                                                                                                                                                        
ALTER_TABLES_PK = '''
                  ALTER TABLE categories
                      ADD CONSTRAINT pk_categories 
                      PRIMARY KEY (category_id);
    
                  ALTER TABLE customer_customer_demo
                      ADD CONSTRAINT pk_customer_customer_demo_customer_id 
                      PRIMARY KEY (customer_id);
                      
                  ALTER TABLE customer_customer_demo
                      ADD CONSTRAINT pk_customer_customer_demo_type_id 
                      PRIMARY KEY (customer_type_id);
                      
                  ALTER TABLE customer_demographics
                      ADD CONSTRAINT pk_customer_demographics 
                      PRIMARY KEY (customer_type_id);
                      
                  ALTER TABLE customers
                      ADD CONSTRAINT pk_customers 
                      PRIMARY KEY (customer_id);
                      
                  ALTER TABLE employees
                      ADD CONSTRAINT pk_employees 
                      PRIMARY KEY (employee_id);
                      
                  ALTER TABLE employee_territories
                      ADD CONSTRAINT pk_employee_territories_employee_id
                      PRIMARY KEY (employee_id);
                      
                  ALTER TABLE employee_territories
                      ADD CONSTRAINT pk_employee_territories_territory_id 
                      PRIMARY KEY (territory_id);    
                      
                  ALTER TABLE orders
                      ADD CONSTRAINT pk_orders 
                      PRIMARY KEY (order_id);
                      
                  ALTER TABLE products
                      ADD CONSTRAINT pk_products 
                      PRIMARY KEY (product_id);
                      
                  ALTER TABLE region
                      ADD CONSTRAINT pk_region 
                      PRIMARY KEY (region_id);
                      
                  ALTER TABLE shippers
                      ADD CONSTRAINT pk_shippers 
                      PRIMARY KEY (shipper_id);
                      
                  ALTER TABLE suppliers
                      ADD CONSTRAINT pk_suppliers 
                      PRIMARY KEY (supplier_id);
                      
                  ALTER TABLE territories
                      ADD CONSTRAINT pk_territories 
                      PRIMARY KEY (territory_id);
                      
                  ALTER TABLE us_states
                      ADD CONSTRAINT pk_usstates 
                      PRIMARY KEY (state_id);
                  '''
              
ALTER_TABLES_FK = '''             
                  ALTER TABLE orders
                      ADD CONSTRAINT fk_orders_customers 
                      FOREIGN KEY (customer_id) 
                      REFERENCES customers(customer_id);
                      
                  ALTER TABLE orders
                      ADD CONSTRAINT fk_orders_employees 
                      FOREIGN KEY (employee_id) 
                      REFERENCES employees(employee_id);
                      
                  ALTER TABLE orders
                      ADD CONSTRAINT fk_orders_shippers 
                      FOREIGN KEY (ship_via) 
                      REFERENCES shippers(ship_via);
                      
                  ALTER TABLE products
                      ADD CONSTRAINT fk_products_categories 
                      FOREIGN KEY (category_id) 
                      REFERENCES categories(category_id);
                      
                  ALTER TABLE products
                      ADD CONSTRAINT fk_products_suppliers 
                      FOREIGN KEY (supplier_id) 
                      REFERENCES suppliers(supplier_id);
                      
                  ALTER TABLE territories
                      ADD CONSTRAINT fk_territories_region 
                      FOREIGN KEY (region_id) 
                      REFERENCES region(region_id);
                      
                  ALTER TABLE employee_territories
                      ADD CONSTRAINT fk_employee_territories_territories 
                      FOREIGN KEY (territory_id) 
                      REFERENCES territories(territory_id);
                      
                  ALTER TABLE employee_territories
                      ADD CONSTRAINT fk_employee_territories_employees 
                      FOREIGN KEY (employee_id) 
                      REFERENCES employees(employee_id);
                      
                  ALTER TABLE customer_customer_demo
                      ADD CONSTRAINT fk_customer_customer_demo_customer_demographics 
                      FOREIGN KEY (customer_type_id) 
                      REFERENCES customer_demographics(customer_type_id);
                      
                  ALTER TABLE customer_customer_demo
                      ADD CONSTRAINT fk_customer_customer_demo_customers 
                      FOREIGN KEY (customer_id) 
                      REFERENCES customers(customer_id);
                      
                  ALTER TABLE employees
                      ADD CONSTRAINT fk_employees_employees 
                      FOREIGN KEY (reports_to) 
                      REFERENCES employees(reports_to);
                      
                  ALTER TABLE order_details
                    ADD CONSTRAINT fk_orders_id
                    FOREIGN KEY (order_id)
                    REFERENCES orders(order_id)
                  '''