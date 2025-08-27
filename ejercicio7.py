import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QRadioButton, QButtonGroup, QPushButton, QComboBox, QCheckBox
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)

       
        self.setStyleSheet("background-color: #f0f4f7;")  

     
        layout = QGridLayout()

     
        titulo = QLabel("Registro de Usuario")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(titulo, 0, 0, 1, 2, alignment=Qt.AlignCenter)

       
        label_usuario = QLabel("Usuario:")
        label_usuario.setStyleSheet("font-size: 14px; color: #34495e;")
        layout.addWidget(label_usuario, 1, 0, alignment=Qt.AlignRight)

        self.input_usuario = QLineEdit()
        self.input_usuario.setStyleSheet("font-size: 14px; padding: 5px;")
        layout.addWidget(self.input_usuario, 1, 1)

        
        label_email = QLabel("Email:")
        label_email.setStyleSheet("font-size: 14px; color: #34495e;")
        layout.addWidget(label_email, 2, 0, alignment=Qt.AlignRight)

        self.input_email = QLineEdit()
        self.input_email.setStyleSheet("font-size: 14px; padding: 5px;")
        layout.addWidget(self.input_email, 2, 1)

    
        label_password = QLabel("Contraseña:")
        label_password.setStyleSheet("font-size: 14px; color: #34495e;")
        layout.addWidget(label_password, 3, 0, alignment=Qt.AlignRight)

        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setStyleSheet("font-size: 14px; padding: 5px;")
        layout.addWidget(self.input_password, 3, 1)

      
        self.checkbox = QCheckBox("Acepto los términos y condiciones")
        self.checkbox.setStyleSheet("font-size: 13px; color: #2c3e50;")
        layout.addWidget(self.checkbox, 4, 0, 1, 2, alignment=Qt.AlignCenter)

       
        self.boton = QPushButton("Registrarse")
        self.boton.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        layout.addWidget(self.boton, 5, 0, 1, 2, alignment=Qt.AlignCenter)

        
        self.setLayout(layout)



app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec_())