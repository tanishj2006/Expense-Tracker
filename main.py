import sys
from PyQt6.QtWidgets import QApplication
from frontend import MainWindow
from expense_class import ExpenseDetails
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())