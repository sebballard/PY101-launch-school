def prompt(message):
    print(f"==> {message}")

def get_float_num(message, is_zero_valid=False):
    prompt(message)

    while True:
        try:
            num_as_str = input()
            num_float = float(num_as_str)

            if (num_float < 0):
                raise ValueError
            if (num_float == 0) and (not is_zero_valid):
                raise ValueError

            break

        except ValueError:
            if is_zero_valid:
                prompt('Please enter a valid number 0 or above')
                prompt('using only digits and max one decimal point')
            else:
                prompt('Please enter a valid number above zero ')
                prompt('containing only digits and max one decimal point')

    return num_float

def get_loan_details():
    loan_amount = get_float_num('What is the amount of the loan? ($)')
    apr_amount = get_float_num('What is the Annual Percentage Rate? ''' +
    '(APR) (%)', True)

    monthly_interest = 0 if apr_amount == 0 else ((apr_amount / 100) / 12)
    duration_months = get_float_num('What is the loan duration in months?')

    return loan_amount, monthly_interest, duration_months

def get_monthly_payment(loan_amount, monthly_interest, duration_months):
    if monthly_interest == 0:
        return loan_amount / duration_months

    return (loan_amount * (monthly_interest / (1 -
            (1 + monthly_interest)**(-duration_months))))


def do_repeat():
    prompt('Do you want to use the mortgage calculator again? (y/n)')
    decision = input().casefold()

    while decision not in ['y', 'n']:
        prompt('Please enter a valid answer! (y/n)')
        decision = input().casefold()

    if decision == 'y':
        return True

    return False


prompt('Welcome to the Mortgage Calculator.')


while True:
    loan_amount, monthly_interest, duration_months = get_loan_details()
    print(loan_amount, monthly_interest, duration_months)
    monthly_payment = get_monthly_payment(
        loan_amount, monthly_interest, duration_months
        )
    print(monthly_payment)

    print(f'The monthly payment is ${round(monthly_payment, 2):.2f}\n')

    if not do_repeat():
        break