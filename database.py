import sqlite3


class Data_base:

    def __init__(self, name = 'system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection(self):
        
        try:
            self.connection.close
        except Exception as e:
            print(e)

#FUNÇÕES DA TABELA DE PRODUTOS

    def create_table_produto(self):

        self.connect()
        myCursor = self.connection.cursor()
        myCursor.execute("""
                    
                    CREATE TABLE IF NOT EXISTS Produto(
                       
                       CODIGO TXT,
                       DESCRICAO TXT,
                       VALOR TXT,
                       

                       PRIMARY KEY(CODIGO)   
                    );

                    """)
        self.close_connection()

    def register_produto(self, fullDataSet):
        
        self.connect()
        campos_tabela = ('CODIGO', 'DESCRICAO', 'VALOR')
        qtde = ("?,?,?")
        myCursor = self.connection.cursor()

        try:
            myCursor.execute(f"""INSERT INTO Produto {campos_tabela}

                VALUES ({qtde})""", fullDataSet)
            
            self.connection.commit()
            return 'ok', "Produto cadastrado com sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)
        
        finally:
            self.close_connection()

    def select_all_produtos(self):
        
        try:
            self.connect()
            myCursor = self.connection.cursor()
            myCursor.execute("SELECT * FROM Produto ORDER BY CODIGO")
            produtos = myCursor.fetchall()
            return produtos
        except Exception as e:
            print(e)
        finally:
            self.close_connection()
    
    def delete_produto(self, codigo):
        
        try:
            self.connect()
            myCursor = self.connection.cursor()
            myCursor.execute(f"DELETE FROM Produto WHERE CODIGO = '{codigo}'")
            self.connection.commit()
            return 'ok', "Produto deletado com sucesso!"
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

    def update_produto(self, fullDataSet):
        
        self.connect()
        try:
            myCursor = self.connection.cursor()
            myCursor.execute(f""" UPDATE Produto set

                        CODIGO = '{fullDataSet[0]}',
                        DESCRICAO = '{fullDataSet[1]}',
                        VALOR = '{fullDataSet[2]}'
                        

                        WHERE CODIGO = '{fullDataSet[0]}'   """)
            self.connection.commit()
            return 'ok', 'Produto alterado com sucesso!'

        except Exception as e:
            return 'erro' 'e'
        finally:
            self.close_connection()

#FUNÇÕES DA TABELA DE CLIENTES

    def create_table_cliente(self):

        self.connect()
        myCursor = self.connection.cursor()
        myCursor.execute("""
                    
                    CREATE TABLE IF NOT EXISTS Cliente(
                       
                        CPF TXT,
                        NOME TXT,
                        NASCIMENTO TXT,
                        LOGRADOURO TXT,
                        NUMERO TXT,
                        COMPLEMENTO TXT,
                        BAIRRO TXT,
                        MUNICIPIO TXT,
                        UF TXT,
                        CEP TXT,
                        WHATSAPP TXT,
                        TELEFONE TXT,
                        EMAIL TXT,
                       

                       PRIMARY KEY(CPF)   
                    );

                    """)
        self.close_connection()

    def register_cliente(self, fullDataSet):
        
        self.connect()
        campos_tabela = ('CPF', 'NOME', 'NASCIMENTO', 'LOGRADOURO', 'NUMERO', 
                         'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 
                         'CEP', 'WHATSAPP', 'TELEFONE', 'EMAIL')
        qtde = ("?,?,?,?,?,?,?,?,?,?,?,?,?")
        myCursor = self.connection.cursor()

        try:
            myCursor.execute(f"""INSERT INTO Cliente {campos_tabela}

                VALUES ({qtde})""", fullDataSet)
            
            self.connection.commit()
            return 'ok', "Cliente cadastrado com sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)
        
        finally:
            self.close_connection()

    def select_all_clientes(self):
        
        try:
            self.connect()
            myCursor = self.connection.cursor()
            myCursor.execute("SELECT * FROM Cliente ORDER BY CPF")
            clientes = myCursor.fetchall()
            return clientes
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def delete_cliente(self, cpf):
        
        try:
            self.connect()
            myCursor = self.connection.cursor()
            myCursor.execute(f"DELETE FROM Cliente WHERE CPF = '{cpf}'")
            self.connection.commit()
            return 'ok', "Cliente deletado com sucesso!"
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

    def update_cliente(self, fullDataSet):
        
        self.connect()
        try:
            myCursor = self.connection.cursor()
            myCursor.execute(f""" UPDATE Cliente set

                        CPF = '{fullDataSet[0]}',
                        NOME = '{fullDataSet[1]}',
                        NASCIMENTO = '{fullDataSet[2]}',
                        LOGRADOURO = '{fullDataSet[3]}',
                        NUMERO = '{fullDataSet[4]}',
                        COMPLEMENTO = '{fullDataSet[5]}',
                        BAIRRO = '{fullDataSet[6]}',
                        MUNICIPIO = '{fullDataSet[7]}',
                        UF = '{fullDataSet[8]}',
                        CEP = '{fullDataSet[9]}',
                        WHATSAPP = '{fullDataSet[10]}',
                        TELEFONE = '{fullDataSet[11]}',
                        EMAIL = '{fullDataSet[12]}'
                        

                        WHERE CPF = '{fullDataSet[0]}'   """)
            self.connection.commit()
            return 'ok', 'Cliente alterado com sucesso!'

        except Exception as e:
            return 'erro' 'e'
        finally:
            self.close_connection()

#FUNÇÃO DA TABELA DE PEDIDOS

    def create_table_pedido(self):
        self.connect()
        myCursor = self.connection.cursor()
        myCursor.execute("""
                    
                    CREATE TABLE IF NOT EXISTS Pedido(
                       
                        NUMPED TXT,
                        CPFPEDIDO TXT,
                        CLIENTE TXT,
                        CODPEDIDO TXT,
                        DESCPEDIDO TXT,
                        QUANTIDADE TXT,
                        VALORTOTAL TXT,
                       

                       PRIMARY KEY(NUMPED)   
                    );

                    """)
        self.close_connection()
    
    def register_pedido(self, fullDataSet):
        self.connect()
        campos_tabela = ('NUMPED', 'CPFPEDIDO', 'CLIENTE', 'CODPEDIDO', 'DESCPEDIDO', 'QUANTIDADE', 'VALORTOTAL')
        qtde = ("?,?,?,?,?,?,?")
        myCursor = self.connection.cursor()

        try:
            myCursor.execute(f"""INSERT INTO Pedido {campos_tabela}

                VALUES ({qtde})""", fullDataSet)
            
            self.connection.commit()
            return 'ok', "Pedido cadastrado com sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)
        
        finally:
            self.close_connection()
    
    def select_all_pedidos(self):
        try:
            self.connect()
            myCursor = self.connection.cursor()
            myCursor.execute("SELECT * FROM Pedido ORDER BY NUMPED")
            pedidos = myCursor.fetchall()
            return pedidos
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def delete_pedidos(self, numpedido):
        
        try:
            self.connect()
            myCursor = self.connection.cursor()
            myCursor.execute(f"DELETE FROM Pedido WHERE NUMPED = '{numpedido}'")
            self.connection.commit()
            return 'ok', "Pedido deletado com sucesso!"
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

    def update_pedido(self, fullDataSet):

        self.connect()
        try:
            myCursor = self.connection.cursor()
            myCursor.execute(f""" UPDATE Pedido set

                        NUMPED = '{fullDataSet[0]}',
                        CLIENTE = '{fullDataSet[1]}'
                        DESCPEDIDO = '{fullDataSet[2]}',
                        QUANTIDADE = '{fullDataSet[3]}',
                        VALORTOTAL = '{fullDataSet[4]}'
                        

                        WHERE NUMPED = '{fullDataSet[0]}'   """)
            self.connection.commit()
            return 'ok', 'Pedido alterado com sucesso!'

        except Exception as e:
            return 'erro' 'e'
        finally:
            self.close_connection()

#FUNÇÃO PARA BUSCAR DADOS DO CLIENTE

    def select_cliente_pedido(self, cpf_pd):
        try:
            self.connect()
            myCursor = self.connection.cursor()
            myCursor.execute(f"SELECT * FROM Cliente WHERE CPF = '{cpf_pd}'")
            #myCursor.execute(f"SELECT * FROM Cliente WHERE REPLACE(CPF, '.', '') = REPLACE(?, '.', '') AND REPLACE(CPF, '-', '') = REPLACE(?, '-', '')", {cpf})
            clientes = myCursor.fetchall()
            return clientes
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

#FUNÇÃO PARA BUSCAR DADOS DO PRODUTO

    def select_produto_pedido(self, cod_pd):
        try:
            self.connect()
            myCursor = self.connection.cursor()
            myCursor.execute(f"SELECT * FROM Produto WHERE CODIGO  = '{cod_pd}'")
            #myCursor.execute(f"SELECT * FROM Cliente WHERE REPLACE(CPF, '.', '') = REPLACE(?, '.', '') AND REPLACE(CPF, '-', '') = REPLACE(?, '-', '')", {cpf})
            produtos = myCursor.fetchall()
            return produtos
        except Exception as e:
            print(e)
        finally:
            self.close_connection()
    
