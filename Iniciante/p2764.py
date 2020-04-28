from datetime import datetime

data = datetime.strptime(input(), '%d/%m/%y')

print(data.strftime('%m/%d/%y'))
print(data.strftime('%y/%m/%d'))
print(data.strftime('%d-%m-%y'))
