import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6 import QtCore
import PySide6.QtWidgets
from ui_main import Ui_MainWindow
from qt_material import apply_stylesheet
from database import Data_base


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Estética & Saúde - SisCad")
        appIcon = QIcon("icon-flor-de-lotus.png")
        self.setWindowIcon(appIcon)

        self.db = Data_base()
        self.busca_produto()
        self.busca_cliente()

        #############################################
        #BOTÃO MENU
        self.btn_menu.clicked.connect(self.leftMenu)
        #############################################


        ####################################################################################################
        #PÁGINAS DO SISTEMA#
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_cad_produto.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cad_produto))
        self.btn_cad_cliente.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cad_cliente))
        self.btn_cad_pedido.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cad_pedido))
        self.btn_historico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_consulta_historico))
        ####################################################################################################

        #############################################
        #CADASTRAR PRODUTOS
        self.btn_cadastrar_produto.clicked.connect(self.cadastro_produto)
        #CADASTRAR CLIENTES
        self.btn_cadastrar_cliente.clicked.connect(self.cadastro_cliente)

        #ALTERAR PRODUTO
        self.btn_alterar_prod.clicked.connect(self.alterar_produto)
        #ALTERAR CLIENTE
        self.btn_alterar_cli.clicked.connect(self.alterar_cliente)

        #EXCLUIR PRODUTO
        self.btn_excluir_prod.clicked.connect(self.excluir_produto)
        #EXCLUIR CLIENTE
        self.btn_excluir_cli.clicked.connect(self.excluir_cliente)
        ##############################################


    def leftMenu(self):
        width = self.left_frame.width()

        if width == 0:
            newWidth = 230
        else:
            newWidth = 0
        
        self.animation = QtCore.QPropertyAnimation(self.left_frame, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def cadastro_produto(self):
        fullDataSet = (
            self.txt_codigo.text(), 
            self.txt_descricao.text(), 
            self.txt_valor.text(),
            
        )
        

        if any(x.strip() == '' for x in fullDataSet):
          self.msg('erro', 'Preencha todos os campos')
          return
        
        #CADASTRAR NO BANCO
        resposta = self.db.register_produto(fullDataSet)

        self.msg(resposta[0],resposta[1])
        self.busca_produto()

    def cadastro_cliente(self):
        fullDataSet = (
            self.txt_cpf.text(), 
            self.txt_nome.text(), 
            self.txt_dt_nascimento.text(),
            self.txt_logradouro.text(),
            self.txt_numero.text(),
            self.txt_complemento.text(),
            self.txt_bairro.text(),
            self.txt_municipio.text(),
            self.txt_uf.text(),
            self.txt_cep.text(),
            self.txt_whatsapp.text(),
            self.txt_telefone.text(),
            self.txt_email.text()
            
        )
        

#        if any(x.strip() == '' for x in fullDataSet):
#          self.msg('erro', 'Preencha todos os campos')
#          return
        
        #CADASTRAR NO BANCO
        resposta = self.db.register_cliente(fullDataSet)
        

        self.msg(resposta[0],resposta[1])
        self.busca_cliente()


    def msg(self, tipo, mensage):
        msg = QMessageBox()
        if tipo.lower() == 'ok':
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Concluído")
        elif tipo.lower() == 'erro':
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Não Concluído")
        elif tipo.lower() == 'aviso':
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Não Concluído")
        
        msg.setText(mensage)
        msg.exec()

#FUNÇÕES DO CADASTRO DE PRODUTO

    def busca_produto(self):
        result = self.db.select_all_produtos()
        self.tb_cad_produto.clearContents()
        self.tb_cad_produto.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_cad_produto.setItem(row, column, QTableWidgetItem(str(data)))
    
    def alterar_produto(self):
        dados = []
        alterar_dados = []

        for row in range(self.tb_cad_produto.rowCount()):
            for column in range(self.tb_cad_produto.columnCount()):
                dados.append(self.tb_cad_produto.item(row, column).text())

            alterar_dados.append(dados)
            dados = []
        
        for prod in alterar_dados:
            result = self.db.update_produto(tuple(prod))

        self.msg(result[0], result[1])
        self.busca_produto()

    def excluir_produto(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Excluir")
        msgBox.setText("Este produto será excluído!")
        msgBox.setInformativeText("Tem certeza que deseja continuar?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msgBox.exec()
        if resp == QMessageBox.Yes:
            codigo = self.tb_cad_produto.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = self.db.delete_produto(codigo)
            self.busca_produto()

            self.msg(result[0],result[1])

#FUNÇÕES DO CADASTRO DE CLIENTE

    def busca_cliente(self):
        result = self.db.select_all_clientes()
        self.tb_cad_cliente.clearContents()
        self.tb_cad_cliente.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_cad_cliente.setItem(row, column, QTableWidgetItem(str(data)))

    def alterar_cliente(self):
        dados = []
        alterar_dados = []

        for row in range(self.tb_cad_cliente.rowCount()):
            for column in range(self.tb_cad_cliente.columnCount()):
                dados.append(self.tb_cad_cliente.item(row, column).text())

            alterar_dados.append(dados)
            dados = []
        
        for prod in alterar_dados:
            result = self.db.update_cliente(tuple(prod))

        self.msg(result[0], result[1])
        self.busca_cliente()

    def excluir_cliente(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Excluir")
        msgBox.setText("Este cliente será excluído!")
        msgBox.setInformativeText("Tem certeza que deseja continuar?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msgBox.exec()
        if resp == QMessageBox.Yes:
            codigo = self.tb_cad_cliente.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = self.db.delete_cliente(codigo)
            self.busca_cliente()

            self.msg(result[0],result[1])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_red.xml')
    db = Data_base()
    db.create_table_produto()
    db.create_table_cliente()
    window = MainWindow()
    window.show()
    app.exec()