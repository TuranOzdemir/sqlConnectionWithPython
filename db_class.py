from configparser import ConfigParser
class db_conf:
    def __init__(self, path):
        self.config = ConfigParser()
        self.config.read(path)
        
       

    def read(self,dbname):
        dict_db = {}
        dict_db['hostname'] = self.config[dbname]['hostname']
        dict_db['database'] = self.config[dbname]['database']
        dict_db['username'] = self.config[dbname]['username']
        dict_db['pasw'] = self.config[dbname]['pasw']
        dict_db['port'] = self.config[dbname]['port']
        return dict_db
    
        
#dbname = 'demo'
#db = db_conf('db_conn_conf.ini')
#db_info = db.read(dbname)
