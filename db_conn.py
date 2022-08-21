import psycopg2
import psycopg2.extras
from configparser import ConfigParser
from config_class import db_conf 


dbname = 'demo'
db_conf =  db_conf('db_conn_conf.ini')
db_info = db_conf.read(dbname)


## CONNECTION INFO (TAKING FROM CONFIGRATION CLASS -> CLASS TAKES IT FROM 'config.ini' file ) 
hostname = db_info['hostname']
database = db_info['database']
username = db_info['username']
pasw =  db_info['pasw']
port = db_info['port']

conn = None

# ---------------- DB CONNECTİON STARTS HERE --------------------------
try:
    with psycopg2.connect(
        host = nameIt.hostname,
        dbname = database,
        user = username,
        password = pasw,
        port = port 
    )   as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
# We delete and recreate the table each time so that the old data does not overlap while the new data is being recorded.
            cur.execute('DROP TABLE IF EXISTS employee')
# ****************** SQL SCRIPTS STARTS HERE***************

        # CREATE NEW TABLE:
            create_script = '''CREATE TABLE IF NOT EXISTS employee(
                id INT PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                salary INT,
                dept_id VARCHAR(30))'''
        # EXECUTE 'create_script'    
            cur.execute(create_script)
        
        # INSERT INTO [table_name]: 
            insert_script = '''INSERT INTO employee(id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'''
            insert_values = [(1,'james', 28000, 'D1'),(2,'David', 20000, 'D1'),(3,'Robin', 5000, 'D2')]
            for record in insert_values:
                cur.execute(insert_script, record)

        # UPDATE SCRİPT:
            update_script = '''UPDATE employee SET salary = salary + (salary * 0.1)'''
            cur.execute(update_script)
        
        # DELETE SCRIPT:
            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('james',)
            cur.execute(delete_script, delete_record)
        
        
        # ACCESSİNG TO DATA 'SELECT * FROM [table_name]'
            cur.execute('SELECT * FROM employee')
            for r in cur.fetchall():
                print(r['name'], r['salary'])

# ****************** SQL SCRIPTS ENDS HERE***************

# It will notify the user if there is an error in the connection information or sql scripts 
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        
# ---------------- DB CONNECTİİON ENDS HERE ----------------------  
