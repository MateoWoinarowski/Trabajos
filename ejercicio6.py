import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QRadioButton, QButtonGroup, QPushButton, QComboBox, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)

        
        layout = QGridLayout()

        
        titulo = QLabel("Registro de Usuario")
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo, 0, 0, 1, 2)

        
        layout.addWidget(QLabel("Usuario:"), 1, 0)
        self.input_usuario = QLineEdit()
        layout.addWidget(self.input_usuario, 1, 1)

    
        layout.addWidget(QLabel("Email:"), 2, 0)
        self.input_email = QLineEdit()
        layout.addWidget(self.input_email, 2, 1)

        
        layout.addWidget(QLabel("Contraseña:"), 3, 0)
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)  
        layout.addWidget(self.input_password, 3, 1)

        
        self.checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.checkbox, 4, 0, 1, 2)

        
        self.boton = QPushButton("Registrarse")
        self.boton.clicked.connect(self.registrar)
        layout.addWidget(self.boton, 5, 0, 1, 2)

        
        self.setLayout(layout)

    def registrar(self):
        usuario = self.input_usuario.text().strip()
        email = self.input_email.text().strip()
        password = self.input_password.text().strip()

        if not usuario or not email or not password:
            QMessageBox.warning(self, "Error", "Debes completar todos los campos.")
            return

        if not self.checkbox.isChecked():
            QMessageBox.warning(self, "Error", "Debes aceptar los términos y condiciones.")
            return

        QMessageBox.information(self, "Éxito", "Registro completado con éxito.")



app = QApplication(sys.argv)
screen= Ventana()
screen.show()
sys.exit(app.exec_())