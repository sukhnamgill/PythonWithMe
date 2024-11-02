import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup, QPoint

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Animated Login Page")
        self.setGeometry(500, 200, 350, 450)
        self.setWindowIcon(QIcon("icon.png"))  # Optional: Set your own icon here

        # Fonts
        font = QFont("Arial", 12)
        title_font = QFont("Arial", 20, QFont.Bold)

        # Title label
        self.title_label = QLabel("Login to Your Account")
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("color: #333; margin-bottom: 20px;")

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #bbb;
                border-radius: 8px;
                background-color: #f0f0f0;
                color: #333;
            }
            QLineEdit:focus {
                border: 1px solid #7e57c2;
                background-color: #ffffff;
            }
        """)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #bbb;
                border-radius: 8px;
                background-color: #f0f0f0;
                color: #333;
            }
            QLineEdit:focus {
                border: 1px solid #7e57c2;
                background-color: #ffffff;
            }
        """)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("""
            QPushButton {
                padding: 10px;
                background-color: #7e57c2;
                color: #ffffff;
                border-radius: 8px;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5e35b1;
            }
            QPushButton:pressed {
                background-color: #4527a0;
            }
        """)
        self.login_button.clicked.connect(self.handle_login)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(15)

        self.setLayout(layout)

        # Background styling
        self.setStyleSheet("QWidget { background-color: #fafafa; }")

        # Start fade-in animation
        self.start_fade_in_animation()

    def start_fade_in_animation(self):
        self.opacity_animation = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_animation.setDuration(1000)  # 1 second
        self.opacity_animation.setStartValue(0)
        self.opacity_animation.setEndValue(1)
        self.opacity_animation.start()

    def start_shake_animation(self):
        animation = QSequentialAnimationGroup(self)
        for i in range(6):  # Shake three times
            move_right = QPropertyAnimation(self, b"pos")
            move_right.setDuration(50)
            move_right.setEndValue(self.pos() + QPoint(10, 0))
            move_right.setEasingCurve(QEasingCurve.OutBounce)

            move_left = QPropertyAnimation(self, b"pos")
            move_left.setDuration(50)
            move_left.setEndValue(self.pos() - QPoint(10, 0))
            move_left.setEasingCurve(QEasingCurve.OutBounce)

            animation.addAnimation(move_right)
            animation.addAnimation(move_left)

        animation.start()

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "password":
            QMessageBox.information(self, "Login Successful", "Welcome!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            self.start_shake_animation()  # Trigger shake on login failure

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())
