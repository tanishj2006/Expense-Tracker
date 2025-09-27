import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QGridLayout, QTableWidget, QTableWidgetItem


class ShowRecordWindow(QDialog):
    def __init__(self,details):
        super().__init__()
        self.details = details
        self.setWindowTitle("Expense Record History")
        self.names = list(details['expense_name'].values())
        self.types = list(details['expense_type'].values())
        self.amounts = list(details['expense_amount'].values())
        self.dates = list(details['expense_time'].values())
        row_wise_data = list(zip(self.names,self.types,self.amounts,self.dates))
        title_label = QLabel("Expense Record History")
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.go_back)
        summary_button = QPushButton("View Summary")
        summary_button.clicked.connect(self.view_summary)
        self.records_table = QTableWidget()
        self.records_table.setColumnCount(4)
        column_headers = ('Name', 'Type', 'Amount', 'Date')
        self.records_table.setHorizontalHeaderLabels(column_headers)
        self.records_table.verticalHeader().setVisible(False)
        for row,data in enumerate(row_wise_data):
            self.records_table.insertRow(row)
            for col,item in enumerate(data):
                self.records_table.setItem(row,col,QTableWidgetItem(str(item)))
        layout = QGridLayout()
        layout.addWidget(title_label,0,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.records_table,1,0,1,0)
        layout.addWidget(back_button,2,1)
        layout.addWidget(summary_button,2,0)
        self.setLayout(layout)

    def go_back(self):
        self.close()

    def view_summary(self):
        summary_window = SummaryButton(pd.DataFrame(self.details).groupby('expense_type')['expense_amount'].sum().reset_index().to_dict())
        summary_window.exec()
        # SummaryButton(self.details).exec()
        # unique_type = set(self.types)
        #
        # type_totals = {expense_type: sum(
        #     amount for amount, typ in zip(self.amounts, self.types) if typ == expense_type
        # ) for expense_type in unique_type}
        #
        # for expense_type, total in type_totals.items():
        #     print(f"You have spent a total of {total} on {expense_type} expenses.")
        #
        # max_type = max(type_totals, key=type_totals.get)
        # max_total = type_totals[max_type]
        # print(f"The expense type with the maximum spending is '{max_type}' with a total of {max_total}.")
        #
        # total_amount = sum(self.amounts)
        # total_expenses = len(self.amounts)
        # print(f"Overall, you made a total purchase of {total_amount} in your last {total_expenses} expenses.")

class SummaryButton(QDialog):
    def __init__(self,details: dict):
        super().__init__()
        self.details = details
        self.types = list(details['expense_type'].values())
        self.amounts = list(details['expense_amount'].values())
        total_amount = sum(self.amounts)

        unique_type = set(self.types)
        type_totals = {expense_type: sum(
            amount for amount, typ in zip(self.amounts, self.types) if typ == expense_type
        ) for expense_type in unique_type}
        max_type = max(type_totals, key=type_totals.get)
        max_total = type_totals[max_type]

        self.amounts = [str(x) for x in self.amounts]
        self.data = list(zip(self.types,self.amounts))
        self.setWindowTitle("Expense Summary")
        title_label = QLabel("Expense Summary")
        category_label = QLabel("Category")
        amount_label = QLabel("Amount")
        total_label = QLabel("Total : ")
        highest_label = QLabel('Highest Category : ')
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.go_back)
        self.layout = QGridLayout()
        self.layout.addWidget(title_label,0,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(category_label,1,0)
        self.layout.addWidget(amount_label,1,1)
        for i, e_type, amount in zip(range(2,len(self.data)+2),self.types,self.amounts):
            self.layout.addWidget(QLabel(e_type),i,0)
            self.layout.addWidget(QLabel(amount),i,1)
        self.layout.addWidget(total_label,len(self.amounts)+2,0)
        self.layout.addWidget(QLabel(str(total_amount)),len(self.amounts)+2,1)
        self.layout.addWidget(highest_label,len(self.amounts)+3,0)
        self.layout.addWidget(QLabel(max_type+', Amount : '+str(max_total)),len(self.amounts)+3,1)
        self.layout.addWidget(back_button,len(self.amounts)+4,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout)


    def go_back(self):
        self.close()