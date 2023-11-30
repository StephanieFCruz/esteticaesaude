# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1077, 776)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(0, 0))
        self.left_frame.setMaximumSize(QSize(0, 16777215))
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_frame = QFrame(self.left_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMinimumSize(QSize(220, 0))
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.logo_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.logo_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.logo_frame, 0, Qt.AlignHCenter)

        self.buttons_frame = QFrame(self.left_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMinimumSize(QSize(220, 0))
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolBox = QToolBox(self.buttons_frame)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 203, 605))
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(185, 35))
        self.btn_home.setMaximumSize(QSize(170, 25))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setIconSize(QSize(14, 14))

        self.verticalLayout_7.addWidget(self.btn_home, 0, Qt.AlignHCenter)

        self.btn_cad_produto = QPushButton(self.page)
        self.btn_cad_produto.setObjectName(u"btn_cad_produto")
        self.btn_cad_produto.setMinimumSize(QSize(185, 35))
        self.btn_cad_produto.setMaximumSize(QSize(170, 25))
        self.btn_cad_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cad_produto.setIconSize(QSize(14, 14))

        self.verticalLayout_7.addWidget(self.btn_cad_produto, 0, Qt.AlignHCenter)

        self.btn_cad_cliente = QPushButton(self.page)
        self.btn_cad_cliente.setObjectName(u"btn_cad_cliente")
        self.btn_cad_cliente.setMinimumSize(QSize(185, 35))
        self.btn_cad_cliente.setMaximumSize(QSize(170, 25))
        self.btn_cad_cliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_cad_cliente, 0, Qt.AlignHCenter)

        self.btn_cad_pedido = QPushButton(self.page)
        self.btn_cad_pedido.setObjectName(u"btn_cad_pedido")
        self.btn_cad_pedido.setMinimumSize(QSize(185, 35))
        self.btn_cad_pedido.setMaximumSize(QSize(170, 25))
        self.btn_cad_pedido.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_cad_pedido, 0, Qt.AlignHCenter)

        self.btn_historico = QPushButton(self.page)
        self.btn_historico.setObjectName(u"btn_historico")
        self.btn_historico.setMinimumSize(QSize(185, 35))
        self.btn_historico.setMaximumSize(QSize(170, 25))
        self.btn_historico.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_historico, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 98, 89))
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.textBrowser = QTextBrowser(self.page_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_15.addWidget(self.textBrowser)

        self.toolBox.addItem(self.page_2, u"Sobre")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.buttons_frame, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.left_frame, 0, Qt.AlignLeft)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu = QPushButton(self.top_frame)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"\n"
"background-color:none;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/Icon-Menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_menu, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_home)
        self.pg_cad_cliente = QWidget()
        self.pg_cad_cliente.setObjectName(u"pg_cad_cliente")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_cad_cliente)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(self.pg_cad_cliente)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tela_cadastrar_cliente = QWidget()
        self.tela_cadastrar_cliente.setObjectName(u"tela_cadastrar_cliente")
        self.verticalLayout_14 = QVBoxLayout(self.tela_cadastrar_cliente)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_3 = QFrame(self.tela_cadastrar_cliente)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.txt_uf = QLineEdit(self.frame_3)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setGeometry(QRect(430, 160, 81, 20))
        self.txt_uf.setAlignment(Qt.AlignCenter)
        self.txt_telefone = QLineEdit(self.frame_3)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(170, 190, 141, 20))
        self.txt_telefone.setMaxLength(13)
        self.txt_telefone.setAlignment(Qt.AlignCenter)
        self.txt_complemento = QLineEdit(self.frame_3)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setGeometry(QRect(480, 130, 181, 20))
        self.txt_complemento.setAlignment(Qt.AlignCenter)
        self.txt_email = QLineEdit(self.frame_3)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(340, 190, 321, 20))
        self.txt_email.setAlignment(Qt.AlignCenter)
        self.txt_municipio = QLineEdit(self.frame_3)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setGeometry(QRect(230, 160, 181, 20))
        self.txt_municipio.setAlignment(Qt.AlignCenter)
        self.txt_logradouro = QLineEdit(self.frame_3)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setGeometry(QRect(10, 130, 351, 20))
        self.txt_logradouro.setAlignment(Qt.AlignCenter)
        self.txt_bairro = QLineEdit(self.frame_3)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(10, 160, 201, 20))
        self.txt_bairro.setAlignment(Qt.AlignCenter)
        self.txt_cpf = QLineEdit(self.frame_3)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(10, 100, 133, 20))
        self.txt_cpf.setMaxLength(11)
        self.txt_cpf.setAlignment(Qt.AlignCenter)
        self.txt_dt_nascimento = QLineEdit(self.frame_3)
        self.txt_dt_nascimento.setObjectName(u"txt_dt_nascimento")
        self.txt_dt_nascimento.setGeometry(QRect(530, 100, 133, 20))
        self.txt_dt_nascimento.setAlignment(Qt.AlignCenter)
        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(150, 100, 371, 20))
        self.txt_nome.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 30, 701, 20))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.txt_numero = QLineEdit(self.frame_3)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setGeometry(QRect(380, 130, 81, 20))
        self.txt_numero.setAlignment(Qt.AlignCenter)
        self.txt_whatsapp = QLineEdit(self.frame_3)
        self.txt_whatsapp.setObjectName(u"txt_whatsapp")
        self.txt_whatsapp.setGeometry(QRect(10, 190, 141, 20))
        self.txt_whatsapp.setMaxLength(13)
        self.txt_whatsapp.setAlignment(Qt.AlignCenter)
        self.btn_cadastrar_cliente = QPushButton(self.frame_3)
        self.btn_cadastrar_cliente.setObjectName(u"btn_cadastrar_cliente")
        self.btn_cadastrar_cliente.setGeometry(QRect(240, 300, 230, 29))
        self.btn_cadastrar_cliente.setMinimumSize(QSize(180, 29))
        self.btn_cadastrar_cliente.setMaximumSize(QSize(230, 29))
        self.btn_cadastrar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.txt_cep = QLineEdit(self.frame_3)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setGeometry(QRect(550, 160, 113, 20))
        self.txt_cep.setMaxLength(9)
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tela_cadastrar_cliente, "")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(310, 20, 131, 20))
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(45, 61, 661, 311))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tb_cad_cliente = QTableWidget(self.layoutWidget)
        if (self.tb_cad_cliente.columnCount() < 13):
            self.tb_cad_cliente.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_cad_cliente.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tb_cad_cliente.setObjectName(u"tb_cad_cliente")

        self.horizontalLayout_6.addWidget(self.tb_cad_cliente)

        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_alterar_cli = QPushButton(self.frame_4)
        self.btn_alterar_cli.setObjectName(u"btn_alterar_cli")

        self.verticalLayout_8.addWidget(self.btn_alterar_cli)

        self.btn_excluir_cli = QPushButton(self.frame_4)
        self.btn_excluir_cli.setObjectName(u"btn_excluir_cli")

        self.verticalLayout_8.addWidget(self.btn_excluir_cli)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.tabWidget.addTab(self.widget, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cad_cliente)
        self.pg_consulta_historico = QWidget()
        self.pg_consulta_historico.setObjectName(u"pg_consulta_historico")
        self.verticalLayout_11 = QVBoxLayout(self.pg_consulta_historico)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget_4 = QTabWidget(self.pg_consulta_historico)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tb_historico = QWidget()
        self.tb_historico.setObjectName(u"tb_historico")
        self.layoutWidget1 = QWidget(self.tb_historico)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(9, 9, 691, 491))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.tab_historico = QTableWidget(self.layoutWidget1)
        if (self.tab_historico.columnCount() < 8):
            self.tab_historico.setColumnCount(8)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tab_historico.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tab_historico.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tab_historico.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tab_historico.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tab_historico.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tab_historico.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tab_historico.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tab_historico.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        self.tab_historico.setObjectName(u"tab_historico")

        self.verticalLayout_17.addWidget(self.tab_historico)

        self.btn_historico_export = QPushButton(self.layoutWidget1)
        self.btn_historico_export.setObjectName(u"btn_historico_export")

        self.verticalLayout_17.addWidget(self.btn_historico_export, 0, Qt.AlignHCenter)

        self.tabWidget_4.addTab(self.tb_historico, "")

        self.verticalLayout_11.addWidget(self.tabWidget_4)

        self.Pages.addWidget(self.pg_consulta_historico)
        self.pg_cad_pedido = QWidget()
        self.pg_cad_pedido.setObjectName(u"pg_cad_pedido")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cad_pedido)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget_2 = QTabWidget(self.pg_cad_pedido)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tela_cad_pedido = QWidget()
        self.tela_cad_pedido.setObjectName(u"tela_cad_pedido")
        self.frame_5 = QFrame(self.tela_cad_pedido)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 30, 701, 401))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 30, 137, 19))
        self.label_5.setBaseSize(QSize(0, 8))
        self.label_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.txt_num_ped = QLineEdit(self.frame_5)
        self.txt_num_ped.setObjectName(u"txt_num_ped")
        self.txt_num_ped.setGeometry(QRect(12, 80, 101, 20))
        self.txt_num_ped.setAlignment(Qt.AlignCenter)
        self.txt_desc = QLineEdit(self.frame_5)
        self.txt_desc.setObjectName(u"txt_desc")
        self.txt_desc.setGeometry(QRect(130, 160, 511, 20))
        self.txt_desc.setAlignment(Qt.AlignCenter)
        self.txt_valorunitario = QLineEdit(self.frame_5)
        self.txt_valorunitario.setObjectName(u"txt_valorunitario")
        self.txt_valorunitario.setGeometry(QRect(170, 200, 151, 20))
        self.txt_valorunitario.setMaxLength(15)
        self.txt_valorunitario.setAlignment(Qt.AlignCenter)
        self.txt_qtde = QLineEdit(self.frame_5)
        self.txt_qtde.setObjectName(u"txt_qtde")
        self.txt_qtde.setGeometry(QRect(10, 200, 111, 20))
        self.txt_qtde.setMaxLength(4)
        self.txt_qtde.setAlignment(Qt.AlignCenter)
        self.txt_cliente = QLineEdit(self.frame_5)
        self.txt_cliente.setObjectName(u"txt_cliente")
        self.txt_cliente.setGeometry(QRect(170, 120, 471, 20))
        self.txt_cliente.setAlignment(Qt.AlignCenter)
        self.btn_cadastrar_pedido = QPushButton(self.frame_5)
        self.btn_cadastrar_pedido.setObjectName(u"btn_cadastrar_pedido")
        self.btn_cadastrar_pedido.setGeometry(QRect(230, 290, 180, 29))
        self.btn_cadastrar_pedido.setMinimumSize(QSize(180, 29))
        self.btn_cadastrar_pedido.setMaximumSize(QSize(230, 29))
        self.btn_cadastrar_pedido.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_pedido.setAutoRepeat(False)
        self.txt_cpf_pedido = QLineEdit(self.frame_5)
        self.txt_cpf_pedido.setObjectName(u"txt_cpf_pedido")
        self.txt_cpf_pedido.setGeometry(QRect(10, 120, 141, 20))
        self.txt_cpf_pedido.setMaxLength(11)
        self.txt_cpf_pedido.setAlignment(Qt.AlignCenter)
        self.txt_cod_pedido = QLineEdit(self.frame_5)
        self.txt_cod_pedido.setObjectName(u"txt_cod_pedido")
        self.txt_cod_pedido.setGeometry(QRect(10, 160, 91, 20))
        self.txt_cod_pedido.setMaxLength(4)
        self.txt_cod_pedido.setAlignment(Qt.AlignCenter)
        self.txt_valortotal = QLineEdit(self.frame_5)
        self.txt_valortotal.setObjectName(u"txt_valortotal")
        self.txt_valortotal.setGeometry(QRect(370, 200, 113, 20))
        self.txt_valortotal.setMaxLength(15)
        self.txt_valortotal.setAlignment(Qt.AlignCenter)
        self.tabWidget_2.addTab(self.tela_cad_pedido, "")
        self.tb_pedidos = QWidget()
        self.tb_pedidos.setObjectName(u"tb_pedidos")
        self.label_10 = QLabel(self.tb_pedidos)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(276, 50, 121, 20))
        self.layoutWidget2 = QWidget(self.tb_pedidos)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(80, 150, 581, 194))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tb_cad_pedido = QTableWidget(self.layoutWidget2)
        if (self.tb_cad_pedido.columnCount() < 8):
            self.tb_cad_pedido.setColumnCount(8)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_cad_pedido.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_cad_pedido.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_cad_pedido.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_cad_pedido.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tb_cad_pedido.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tb_cad_pedido.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tb_cad_pedido.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tb_cad_pedido.setHorizontalHeaderItem(7, __qtablewidgetitem28)
        self.tb_cad_pedido.setObjectName(u"tb_cad_pedido")

        self.horizontalLayout_7.addWidget(self.tb_cad_pedido)

        self.frame_6 = QFrame(self.layoutWidget2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_faturar_pedido = QPushButton(self.frame_6)
        self.btn_faturar_pedido.setObjectName(u"btn_faturar_pedido")

        self.verticalLayout_16.addWidget(self.btn_faturar_pedido)

        self.btn_excluir_pedido = QPushButton(self.frame_6)
        self.btn_excluir_pedido.setObjectName(u"btn_excluir_pedido")

        self.verticalLayout_16.addWidget(self.btn_excluir_pedido)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)


        self.horizontalLayout_7.addWidget(self.frame_6)

        self.tabWidget_2.addTab(self.tb_pedidos, "")

        self.verticalLayout_9.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pg_cad_pedido)
        self.pg_cad_produto = QWidget()
        self.pg_cad_produto.setObjectName(u"pg_cad_produto")
        self.verticalLayout_10 = QVBoxLayout(self.pg_cad_produto)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget_3 = QTabWidget(self.pg_cad_produto)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tela_cadastrar_produto = QWidget()
        self.tela_cadastrar_produto.setObjectName(u"tela_cadastrar_produto")
        self.frame = QFrame(self.tela_cadastrar_produto)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 30, 541, 241))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_valor = QLineEdit(self.frame)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_valor, 5, 0, 1, 1, Qt.AlignLeft)

        self.txt_codigo = QLineEdit(self.frame)
        self.txt_codigo.setObjectName(u"txt_codigo")
        self.txt_codigo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_codigo, 3, 0, 1, 1, Qt.AlignLeft)

        self.txt_descricao = QLineEdit(self.frame)
        self.txt_descricao.setObjectName(u"txt_descricao")
        self.txt_descricao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_descricao, 4, 0, 1, 1, Qt.AlignVCenter)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.btn_cadastrar_produto = QPushButton(self.tela_cadastrar_produto)
        self.btn_cadastrar_produto.setObjectName(u"btn_cadastrar_produto")
        self.btn_cadastrar_produto.setGeometry(QRect(230, 330, 180, 29))
        self.btn_cadastrar_produto.setMinimumSize(QSize(180, 29))
        self.btn_cadastrar_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget_3.addTab(self.tela_cadastrar_produto, "")
        self.tela_produtos = QWidget()
        self.tela_produtos.setObjectName(u"tela_produtos")
        self.verticalLayout_13 = QVBoxLayout(self.tela_produtos)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.tela_produtos)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tb_cad_produto = QTableWidget(self.tela_produtos)
        if (self.tb_cad_produto.columnCount() < 3):
            self.tb_cad_produto.setColumnCount(3)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tb_cad_produto.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tb_cad_produto.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tb_cad_produto.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        self.tb_cad_produto.setObjectName(u"tb_cad_produto")
        self.tb_cad_produto.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_4.addWidget(self.tb_cad_produto)

        self.frame_2 = QFrame(self.tela_produtos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_alterar_prod = QPushButton(self.frame_2)
        self.btn_alterar_prod.setObjectName(u"btn_alterar_prod")
        self.btn_alterar_prod.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.btn_alterar_prod)

        self.btn_excluir_prod = QPushButton(self.frame_2)
        self.btn_excluir_prod.setObjectName(u"btn_excluir_prod")
        self.btn_excluir_prod.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.btn_excluir_prod)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_4)

        self.tabWidget_3.addTab(self.tela_produtos, "")

        self.verticalLayout_10.addWidget(self.tabWidget_3)

        self.Pages.addWidget(self.pg_cad_produto)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.footer_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icon-flor-de-lotus.png\"/></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cad_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.btn_cad_cliente.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
        self.btn_cad_pedido.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Pedido", None))
        self.btn_historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Vendas", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-4f124c95-7fff-088f-3004-6e1e1eea1789\"></a><span style=\" font-family:'Arial,sans-serif'; font-size:10pt; color:#d15394; background-color:transparent;\">O</span><span style=\" font-family:'Arial,sans-serif'; font-size:10pt; color:#d15394; background-color:transparent;\"> SisCad consiste em um sistema comercial simples de presta\u00e7\u00e3o de servi\u00e7os, contando com as funcionalidades de cadastro de produtos, cadastro de clientes, cadastro de pedidos e hist\u00f3rico de vendas.</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#646464;\">Est\u00e9tica &amp; Sa\u00fade - SisCad</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/Est\u00e9tica&amp;Sa\u00fade.png\"/></p></body></html>", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_dt_nascimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cadastro de cliente</span></p></body></html>", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.txt_whatsapp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"WhatsApp", None))
        self.btn_cadastrar_cliente.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela_cadastrar_cliente), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Clientes</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_cad_cliente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem1 = self.tb_cad_cliente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tb_cad_cliente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"NASCIMENTO", None));
        ___qtablewidgetitem3 = self.tb_cad_cliente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem4 = self.tb_cad_cliente.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem5 = self.tb_cad_cliente.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem6 = self.tb_cad_cliente.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem7 = self.tb_cad_cliente.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem8 = self.tb_cad_cliente.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem9 = self.tb_cad_cliente.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem10 = self.tb_cad_cliente.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"WHATSAPP", None));
        ___qtablewidgetitem11 = self.tb_cad_cliente.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem12 = self.tb_cad_cliente.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_alterar_cli.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_cli.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem13 = self.tab_historico.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Numero pedido", None));
        ___qtablewidgetitem14 = self.tab_historico.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem15 = self.tab_historico.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem16 = self.tab_historico.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem17 = self.tab_historico.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem18 = self.tab_historico.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"QTDE", None));
        ___qtablewidgetitem19 = self.tab_historico.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Valor Unit\u00e1rio", None));
        ___qtablewidgetitem20 = self.tab_historico.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Valor Total", None));
        self.btn_historico_export.setText(QCoreApplication.translate("MainWindow", u"Exportar Hist\u00f3rico", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tb_historico), QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cadastro de Pedido</span></p></body></html>", None))
        self.txt_num_ped.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba do Pedido", None))
        self.txt_desc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Produto e/ou Servi\u00e7o", None))
        self.txt_valorunitario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor Unit\u00e1riol R$:", None))
        self.txt_qtde.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.txt_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.btn_cadastrar_pedido.setText(QCoreApplication.translate("MainWindow", u"Emitir Pedido", None))
        self.txt_cpf_pedido.setInputMask("")
        self.txt_cpf_pedido.setText("")
        self.txt_cpf_pedido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_cod_pedido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.txt_valortotal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor Total R$", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tela_cad_pedido), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Pedidos</span></p></body></html>", None))
        ___qtablewidgetitem21 = self.tb_cad_pedido.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"NUMPEDIDO", None));
        ___qtablewidgetitem22 = self.tb_cad_pedido.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"CPFPEDIDO", None));
        ___qtablewidgetitem23 = self.tb_cad_pedido.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem24 = self.tb_cad_pedido.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"CODIGO DO PRODUTO", None));
        ___qtablewidgetitem25 = self.tb_cad_pedido.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"DESCRICAO DO PRODUTO", None));
        ___qtablewidgetitem26 = self.tb_cad_pedido.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"QTDE", None));
        ___qtablewidgetitem27 = self.tb_cad_pedido.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"VALORUNITARIO", None));
        ___qtablewidgetitem28 = self.tb_cad_pedido.horizontalHeaderItem(7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"VALORTOTAL", None));
        self.btn_faturar_pedido.setText(QCoreApplication.translate("MainWindow", u"Faturar", None))
        self.btn_excluir_pedido.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tb_pedidos), QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.txt_valor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor R$", None))
        self.txt_codigo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.txt_descricao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do produto", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cadastro de Produto</span></p></body></html>", None))
        self.btn_cadastrar_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tela_cadastrar_produto), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Produto</span></p></body></html>", None))
        ___qtablewidgetitem29 = self.tb_cad_produto.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem30 = self.tb_cad_produto.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"DESCRICAO", None));
        ___qtablewidgetitem31 = self.tb_cad_produto.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"VALOR R$", None));
        self.btn_alterar_prod.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_prod.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tela_produtos), QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CopyRight Est\u00e9tica & Sa\u00fade - SisCad 2023", None))
    # retranslateUi

