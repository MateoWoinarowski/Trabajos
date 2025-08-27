import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QRadioButton, QButtonGroup, QPushButton, QComboBox, QCheckBox
from PyQt5.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        
        

        
        self.label = QLabel("Registro de Usuario")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label, 0, 0, 1, 2)

        
        self.checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.checkbox, 1, 0, 1, 2)

        
        self.boton = QPushButton("Confirmar")
        self.boton.clicked.connect(self.verificar)
        layout.addWidget(self.boton, 2, 0, 1, 2)

        
        self.mensaje = QLabel("")
        self.mensaje.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.mensaje, 3, 0, 1, 2)

    def verificar(self):
        if self.checkbox.isChecked():
            self.mensaje.setText("Aceptaste los términos y condiciones.")
        else:
            self.mensaje.setText("Tenes que aceptar los términos para continuar.")


app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec_())