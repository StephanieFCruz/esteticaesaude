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
import pandas as pd
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Estética & Saúde - SisCad")
        appIcon = QIcon("lotus_icon.png")
        self.setWindowIcon(appIcon)

        self.db = Data_base()
        self.busca_produto()
        self.busca_cliente()
        self.busca_pedido()
        self.busca_historico()

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
        #####################################################################################################

        ######################################################
        #PREENCHIMENTO AUTOMATICO DOS DADOS NO PEDIDO
        self.txt_cpf_pedido.editingFinished.connect(self.busca_cpf)
        self.txt_cod_pedido.editingFinished.connect(self.busca_codigo)
        self.txt_qtde.editingFinished.connect(self.calcular_total)
        ######################################################
        
        #CADASTRAR PRODUTOS
        self.btn_cadastrar_produto.clicked.connect(self.cadastro_produto)
        #CADASTRAR CLIENTES
        self.btn_cadastrar_cliente.clicked.connect(self.cadastro_cliente)
        #CADASTRAR PEDIDOS
        self.btn_cadastrar_pedido.clicked.connect(self.cadastro_pedido)

        #ALTERAR PRODUTO
        self.btn_alterar_prod.clicked.connect(self.alterar_produto)
        #ALTERAR CLIENTE
        self.btn_alterar_cli.clicked.connect(self.alterar_cliente)

        #EXCLUIR PRODUTO
        self.btn_excluir_prod.clicked.connect(self.excluir_produto)
        #EXCLUIR CLIENTE
        self.btn_excluir_cli.clicked.connect(self.excluir_cliente)
        #EXCLUIR PEDIDO
        self.btn_excluir_pedido.clicked.connect(self.excluir_pedido)

        #FATURAR PEDIDOS
        self.btn_faturar_pedido.clicked.connect(self.faturar_pedido)

        #EXTRAIR EXCEL
        self.btn_historico_export.clicked.connect(self.excel_export)

    def leftMenu(self):
        width = self.left_frame.width()

        if width == 0:
            newWidth = 250
        else:
            newWidth = 0
        
        self.animation = QtCore.QPropertyAnimation(self.left_frame, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

#FUNÇÕES DE CADASTRO

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

        if any(x.strip() == '' for x in fullDataSet):
          self.msg('erro', 'Preencha todos os campos')
          return
        
        #CADASTRAR NO BANCO
        resposta = self.db.register_cliente(fullDataSet)  

        self.msg(resposta[0],resposta[1])
        self.busca_cliente()

    def cadastro_pedido(self):
        fullDataSet = (
            self.txt_num_ped.text(), 
            self.txt_cpf_pedido.text(),
            self.txt_cliente.text(),
            self.txt_cod_pedido.text(),
            self.txt_desc.text(),
            self.txt_qtde.text(), 
            self.txt_valorunitario.text(),
            self.txt_valortotal.text(),
            
        )
               
        if any(x.strip() == '' for x in fullDataSet):
          self.msg('erro', 'Preencha todos os campos')
          return
        
        #CADASTRAR NO BANCO
        resposta = self.db.register_pedido(fullDataSet)
        
        self.msg(resposta[0],resposta[1])
        self.busca_pedido()

#FUNÇÃO DE FATURAR

    def faturar_pedido(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Faturar")
        msgBox.setText("Este pedido será faturado!")
        msgBox.setInformativeText("Tem certeza que deseja continuar?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msgBox.exec()
        if resp == QMessageBox.Yes:
            
            pedidofechado = self.tb_cad_pedido.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = self.db.pedido_historico(pedidofechado)
            self.db.delete_pedidos(pedidofechado)
            self.msg(result[0],result[1])
            self.busca_pedido()
            self.busca_historico()

#FUNÇÕES DE BUSCA

    def busca_cpf(self):
        cpf_pd = self.txt_cpf_pedido.text()
        self.db.select_cliente_pedido(cpf_pd)
        campoCpf = self.db.select_cliente_pedido(cpf_pd)
        self.txt_cliente.setText(campoCpf[0][1])

    def busca_codigo(self):
        cod_pd = self.txt_cod_pedido.text()
        self.db.select_produto_pedido(cod_pd)
        campoCod = self.db.select_produto_pedido(cod_pd)
        self.txt_desc.setText(campoCod[0][1])
        self.txt_valorunitario.setText(campoCod[0][2])

#FUNÇÃO DE CALCULO DO TOTAL

    def calcular_total(self):
        qtde_item = float(self.txt_qtde.text())
        calc_total = float(self.txt_valorunitario.text())
        self.txt_valortotal.setText(str(float(calc_total) * float(qtde_item)))

#FUNÇÃO DE MENSAGENS

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
            msg.setWindowTitle("Verifique")
        
        msg.setText(mensage)
        msg.exec()

#FUNÇÕES DA TELA DE PRODUTO

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

#FUNÇÕES DA TELA DE CLIENTE

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

#FUNÇÕES DA TELA DE PEDIDO

    def busca_pedido(self):
        result = self.db.select_all_pedidos()
        self.tb_cad_pedido.clearContents()
        self.tb_cad_pedido.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_cad_pedido.setItem(row, column, QTableWidgetItem(str(data)))

    def alterar_pedido(self):
        dadosPedido = []
        alterar_dadosPedido = []

        for row in range(self.tb_cad_pedido.rowCount()):
            for column in range(self.tb_cad_pedido.columnCount()):
                dadosPedido.append(self.tb_cad_pedido.item(row, column).text())

            alterar_dadosPedido.append(dadosPedido)
            dadosPedido = []
        print("Chegou aqui!")
        for prod in alterar_dadosPedido:
            result = self.db.update_pedido(tuple(prod))

        self.msg(result[0], result[1])
        self.busca_pedido()

    def excluir_pedido(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Excluir")
        msgBox.setText("Este pedido será excluído!")
        msgBox.setInformativeText("Tem certeza que deseja continuar?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msgBox.exec()
        if resp == QMessageBox.Yes:
            codigo = self.tb_cad_pedido.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = self.db.delete_pedidos(codigo)
            self.busca_pedido()

            self.msg(result[0],result[1])

#FUNÇÃO EXPORTAR HISTORICO

    def excel_export(self):
        cnx = sqlite3.connect('system.db')

        historico = pd.read_sql_query("""SELECT * FROM Historico""", con=cnx)
        historico.to_excel("Historico.xlsx", sheet_name='Historico', index=False)

        self.msg('ok', "Histórico extraído com sucesso!")

#FUNÇÃO DA TELA DE HISTORICO

    def busca_historico(self):
        result = self.db.select_all_historico()
        self.tab_historico.clearContents()
        self.tab_historico.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tab_historico.setItem(row, column, QTableWidgetItem(str(data)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_red.xml')
    db = Data_base()
    db.create_table_produto()
    db.create_table_cliente()
    db.create_table_pedido()
    db.create_table_hist()
    window = MainWindow()
    window.show()
    app.exec()