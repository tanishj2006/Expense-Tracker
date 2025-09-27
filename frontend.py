from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout, QPushButton, QMessageBox, QDialog, QLineEdit, \
    QComboBox, QCalendarWidget

from expense_class import ExpenseDetails
from show_record_file import ShowRecordWindow
from expense_class import ShowingDetails


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance Management App")
        title_label = QLabel("Finance Management App")
        show_expense_window_button = QPushButton("Show Expense Records")
        show_expense_window_button.clicked.connect(self.show_expense_window)
        log_expense_window_button = QPushButton("Log new Expense")
        log_expense_window_button.clicked.connect(self.log_expense_window)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close_window)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QGridLayout()
        layout.addWidget(title_label,0,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(show_expense_window_button,1,0)
        layout.addWidget(log_expense_window_button,1,1)
        layout.addWidget(exit_button,2,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralWidget.setLayout(layout)

    def log_expense_window(self):
        log_expense_window = LogExpenseWindow()
        log_expense_window.exec()

    def show_expense_window(self):
        showing_details = ShowingDetails()
        details = showing_details.show_expense()
        show_expense_window = ShowRecordWindow(details)
        show_expense_window.exec()

    def close_window(self):
        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Close Window?")
        confirmation_widget.setText("Are you sure you want to exit the App?")
        confirmation_widget.setIcon(QMessageBox.Icon.Question)
        confirmation_widget.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        confirm = confirmation_widget.exec()
        if confirm == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            confirmation_widget.close()

class LogExpenseWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log New Expense")
        expense_label = QLabel("Log new expense")
        self.pop_up_of_non_numeric = False
        name_label = QLabel("Expense Name :")
        type_label = QLabel("Expense Type :")
        amount_label = QLabel("Amount :")
        date_label = QLabel("Select Date :")
        self.name_input = QLineEdit()
        self.name_input.setToolTip("Give Name of the Expense, Eg: Chocolate")
        self.type_input = QComboBox()
        expense_type_list = [
            'Education','Travel','Groceries','Rent','Utilities','Investment','Medical','Pharmaceuticals','Maintenance','Taxes','Loan EMIs','Hygiene','Entertainment','Food','Vacation(holidays)','Fashion','Shopping','Self Care','Miscellaneous'
        ]
        self.amount_input = QLineEdit()
        self.amount_input.setToolTip("Give Amount only in numeric value eg: 5000.23")
        self.type_input.addItems(expense_type_list)
        self.calender = QCalendarWidget()
        self.calender.setGridVisible(True)
        self.calender.setMaximumDate(QDate.currentDate())
        log_expense_button = QPushButton("Record Expense")
        log_expense_button.clicked.connect(self.log_expense)
        layout = QGridLayout()
        layout.addWidget(expense_label,0,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(name_label,1,0)
        layout.addWidget(self.name_input,1,1)
        layout.addWidget(type_label,2,0)
        layout.addWidget(self.type_input,2,1)
        layout.addWidget(amount_label,3,0)
        layout.addWidget(self.amount_input,3,1)
        layout.addWidget(date_label,4,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.calender,5,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(log_expense_button,6,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def log_expense(self):
        name = self.name_input.displayText()
        amount = self.amount_input.displayText()
        try:
            amount = float(amount)
        except ValueError:
            self.amount_input.clear()
            amount = 0.0
            self.pop_up_of_non_numeric = True
            if len(name) != 0:
                warning_widget = QMessageBox()
                warning_widget.setWindowTitle("Unacceptable Input")
                warning_widget.setText("Please check the amount may not be numeric")
                warning_widget.setIcon(QMessageBox.Icon.Warning)
                warning_widget.setStandardButtons(QMessageBox.StandardButton.Ok)
                confirm = warning_widget.exec()
                if confirm == QMessageBox.StandardButton.Ok:
                    warning_widget.close()
            if len(name.strip()) == 0:
                self.pop_up_of_non_numeric = False
        type_exp = self.type_input.currentText()
        date = self.calender.selectedDate().toString()
        if len(name.strip()) != 0 and amount > 0:
            expense_details = ExpenseDetails(
                name=name,
                type_exp=type_exp,
                amount=amount,
                date=date
            )
            expense_details.log_expense()
            del expense_details
            confirmation_widget = QMessageBox()
            confirmation_widget.setWindowTitle("Success")
            confirmation_widget.setText("Expense Logged Successfully\n"
                                        "Do you want to log a new expense")
            confirmation_widget.setIcon(QMessageBox.Icon.Question)
            confirmation_widget.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirm = confirmation_widget.exec()
            if confirm == QMessageBox.StandardButton.Yes:
                self.amount_input.clear()
                self.name_input.clear()
                confirmation_widget.close()
            else:
                confirmation_widget.close()
                self.close()
        else:
            if not self.pop_up_of_non_numeric:
                warning_widget = QMessageBox()
                warning_widget.setWindowTitle("Unacceptable Input")
                warning_widget.setText("Please check data some of your field may be empty")
                warning_widget.setIcon(QMessageBox.Icon.Warning)
                warning_widget.setStandardButtons(QMessageBox.StandardButton.Ok)
                confirm = warning_widget.exec()
                if confirm == QMessageBox.StandardButton.Ok:
                    warning_widget.close()

