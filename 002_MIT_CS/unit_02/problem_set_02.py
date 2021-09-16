# Credit card balance over one year.

# balance - the outstanding balance on the credit card

# for balance in [1000, -1000, 0, 100, -100]:
# monthlyPaymentRate = 0.02
# annualInterestRate = 0.18

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
for month in range(1, 13):
    monthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - monthlyPayment
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
print("Remaining balance:", round(balance, 2))

# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
# Test Case 1:
# balance = 3329
# annualInterestRate = 0.2
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310

monthlyInterestRate = annualInterestRate / 12.0
balance = 3329
# calculate the lowest payment

monthlyPaymentRate = 0
total = balance
remaining = balance
monthlyInterestRate = annualInterestRate / 12.0

while balance > 0:
    for month in range(12):
        remaining = remaining - monthlyPaymentRate + ((remaining - monthlyPaymentRate) * monthlyInterestRate)
    if remaining > 0:
        monthlyPaymentRate += 10
        remaining = total
    elif remaining <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)

init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
E = 0.03

while abs(balance) > E:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > E:
        lower = monthlyPaymentRate
    elif balance < -E:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))