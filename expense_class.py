import os.path
import pandas as pd



class ExpenseDetails:
    def __init__(self,name,type_exp,date,amount):
        self.file_name = 'expense_records.csv'
        self.expense_name = name
        self.expense_type = type_exp
        self.expense_amount = amount
        self.expense_date = date
        self.expense_detail = {
            'expense_name':[],
            'expense_type':[],
            'expense_amount':[],
            'expense_time':[]
         }
        self.expense_list = []
        self.df =None

    def log_expense (self):
        self.expense_detail['expense_amount'].append(self.expense_amount)
        self.expense_detail['expense_type'].append(self.expense_type)
        self.expense_detail['expense_time'].append(self.expense_date)
        self.expense_detail['expense_name'].append(self.expense_name)
        self.df = pd.DataFrame(self.expense_detail)
        # file handling
        if os.path.exists(self.file_name):
            file_exists=True
        else:
            with (open(self.file_name, 'w') as file):
                file.write(','.join(list(self.expense_detail.keys()))+'\n')
                file_exists=True

        # file_exists = os.path.isfile('expense_records.csv')
        self.df.to_csv(self.file_name, index=False, mode='a', header=not file_exists)


class ShowingDetails:
    def __init__(self):
        self.file_name = 'expense_records.csv'

    def show_expense(self):
       read_df = pd.read_csv(self.file_name)
       details = read_df.to_dict()
       return details