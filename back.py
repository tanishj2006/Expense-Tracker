# from expense_class import ExpenseDetails
# from expense_class import ShowingDetails
#
# details = ShowingDetails()
# k = details.show_expense()[1]
# details = details.show_expense()[0]
# names = list(details['expense_name'].values())
# types = list(details['expense_type'].values())
# amounts = list(details['expense_amount'].values())
# dates = list(details['expense_time'].values())
# print(names)
# print(types)
# print(amounts)
# print(dates)
# row_datas = list(zip(names, types, amounts, dates))
# print(row_datas)

# import pandas as pd
# import numpy as np
# num = np.random.randint(1000,9999,size=5)
# df = pd.DataFrame(num, columns=['OTP'])
# print(str(df))

# import random
#
# digits = [i for i in range(10)]
# random_num = ''
# for i in range(4):
#     random_num += str(random.choice(digits))
# print(random_num)

import pandas as pd

# Sample DataFrame
data = {'name': ['A', 'B', 'A', 'C', 'B', 'C'],
        'type': ['X', 'Y', 'Y', 'X', 'X', 'Y'],
        'amount': [10, 5, 12, 8, 15, 7]}
df = pd.DataFrame(data)

# Group by 'name' and 'type' and sum 'amount'
summary = df.groupby(['name', 'type'])['amount'].sum()

# Sort the summary by 'name' (ascending) and 'amount' (descending)
summary_sorted = summary.sort_values(ascending=[True])

# Print the sorted summary
print(summary_sorted)


#To reset index
summary_sorted = summary_sorted.reset_index()
print(summary_sorted)
