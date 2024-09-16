import numpy as np
import matplotlib.pyplot as plt

def calculate_emi(principal, annual_rate, tenure_years):
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate)**tenure_months) / ((1 + monthly_rate)**tenure_months - 1)
    return emi, tenure_months

def generate_loan_schedule(principal, annual_rate, tenure_years, pre_close_month=None):
    emi, tenure_months = calculate_emi(principal, annual_rate, tenure_years)
    balance = principal
    interest_paid = 0
    emi_schedule = []

    for month in range(1, tenure_months + 1):
        monthly_interest = balance * (annual_rate / 12 / 100)
        principal_payment = emi - monthly_interest
        balance -= principal_payment
        interest_paid += monthly_interest

        emi_schedule.append((month, round(emi, 2), round(monthly_interest, 2), round(principal_payment, 2), round(balance, 2)))

        if pre_close_month is not None and month == pre_close_month:
            break

    return emi_schedule, interest_paid, tenure_months

def calculate_interest_lost(principal, annual_rate, tenure_years, pre_close_month):
    full_schedule, full_interest_paid, _ = generate_loan_schedule(principal, annual_rate, tenure_years)
    pre_close_schedule, pre_close_interest_paid, _ = generate_loan_schedule(principal, annual_rate, tenure_years, pre_close_month)

    interest_lost = full_interest_paid - pre_close_interest_paid
    return interest_lost, pre_close_schedule

def plot_emi_schedule(emi_schedule):
    months = [x[0] for x in emi_schedule]
    balances = [x[4] for x in emi_schedule]
    interests = [x[2] for x in emi_schedule]
    principals = [x[3] for x in emi_schedule]

    plt.figure(figsize=(10, 6))
    plt.plot(months, balances, label='Outstanding Balance', color='blue')
    plt.bar(months, interests, label='Interest Component', color='red', alpha=0.5)
    plt.bar(months, principals, label='Principal Component', color='green', alpha=0.5)

    plt.title('EMI Payment Schedule')
    plt.xlabel('Months')
    plt.ylabel('Amount')
    plt.legend()
    plt.grid(True)
    plt.show()

principal = 500000
annual_rate = 7.5
tenure_years = 20
pre_close_month = 120

emi_schedule, total_interest_paid, _ = generate_loan_schedule(principal, annual_rate, tenure_years)
plot_emi_schedule(emi_schedule)

interest_lost, pre_close_schedule = calculate_interest_lost(principal, annual_rate, tenure_years, pre_close_month)

print(f"Total interest lost due to pre-closure at month {pre_close_month}: {round(interest_lost, 2)}")
