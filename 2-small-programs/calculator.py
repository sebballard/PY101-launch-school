import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

with open('calculator_messages.json', 'r') as file:
    MESSAGES_INIT= json.load(file)





prompt(MESSAGES_INIT['en']['welcome'])

prompt(MESSAGES_INIT['en']['lang_prompt'])

lang = input()

while lang not in ['en', 'es', 'nl']:
    prompt(MESSAGES_INIT['en']['invalid_lang'])
    lang = input()

MESSAGES = MESSAGES_INIT[lang]

while True:
    prompt(MESSAGES['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt(MESSAGES['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt(MESSAGES['operation_prompt'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES['invalid_operation'])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(MESSAGES['result'] + str(output) )

    print()

    prompt(MESSAGES['repeat_prompt'])
    new_calc_choice = input().casefold()

    while new_calc_choice not in ['y', 'n']:
        prompt(MESSAGES['invalid_repeat'])
        new_calc_choice = input()

    if new_calc_choice == 'n':
        break
