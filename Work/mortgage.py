# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000
month = 0
rate = 0.05
payment = 2684.11
extra = 1000
total_paid = 0

while principal > 0:
    month += 1
    if month <= 12:
       the_payment = payment + 1000
    else:
       the_payment = payment
    principal = principal * (1+rate/12) - the_payment
    total_paid = total_paid + the_payment
print('Total paid', round(total_paid, 1))
print('Months', month)
