import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def on_button_click():
    print("Button Clicked!")

app = QApplication(sys.argv)

# Create a main window
window = QWidget()
window.setWindowTitle('My First PyQt Application')

# Create a button
button = QPushButton('Click Me!')
button.clicked.connect(on_button_click)  # Connect button click to function

# Set the layout
layout = QVBoxLayout()
layout.addWidget(button)
window.setLayout(layout)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
