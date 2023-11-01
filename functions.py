import sqlite3
from database import Data_base


def connect(self):
        self.connection = sqlite3.connect(self.name)
        
def consulta_cpf(self):
    self.db = Data_base()
    self.connect()
    

    resp = "SELECT * FROM Cliente WHERE CPF = 12345678910"

    print(resp)

consulta_cpf()
    