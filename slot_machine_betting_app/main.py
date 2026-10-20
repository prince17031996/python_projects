import random
MAX_NO_LINES=3
MIN_NO_LINES=1
MAX_BET_AMOUNT=100
MIN_BET_AMOUNT=1
ROWS=3
COLS=3
symbol_count = {"A":2,"B":4,"C":6,"D":8}
symbol_value = {'A':5,'B':4,'C':6,'D':2}
def deposit():
    while True:
        amount=input("what would you like to deposit?  ")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                print(f"deposited amount is {amount}")
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Please enter a number')
    return amount

def get_number_of_lines():
    while True:
        number_of_lines=input("Enter number of lines to bet (1-"+str(MAX_NO_LINES)+")? ")
        if number_of_lines.isdigit():
            number_of_lines=int(number_of_lines)
            if MIN_NO_LINES<=number_of_lines<=MAX_NO_LINES:
                print(f"Number of lines is {number_of_lines}")
                break
            else:
                print('Number of lines must be between 1 and '+str(MAX_NO_LINES))
        else:
            print('Please enter a number')
    return number_of_lines

def get_bet():
    while True:
        bet_amount=input("How much would  you like to bet on each line?  ")
        if bet_amount.isdigit():
            bet_amount=int(bet_amount)
            if MIN_BET_AMOUNT<=bet_amount<=MAX_BET_AMOUNT:
                print(f"Bet amount is {bet_amount}")
                break
            else:
                print(f'Amount Must be between {MIN_BET_AMOUNT} and {MAX_BET_AMOUNT}')
        else:
            print('Please enter a valid Bet')
    return bet_amount
def put_bet(total_bet,balance):
    while True:
        if total_bet>balance:
            print(f"You dont have enough money to bet {balance - total_bet} is Less than what you want to bet on")
            break
        else:
            print(f"Remaining Balance Post bet is {balance - total_bet}")
            break
    balance=balance-total_bet
    return balance

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")
        print()



def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)

    return winnings,winning_lines


def spin(balance):
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting {bet} on {lines} lines. Total bet is {total_bet} ")
    balance = put_bet(total_bet, balance)
    print(balance, lines, bet)
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"total winning is {winnings}")
    print(f"You won on Lines : ", *winning_line)
    return winnings-total_bet



def __main__():
    balance=deposit()
    while True:
        print(f"Current Balance is {balance}")
        ans = input("Press enter to spin and (q to quit) ")
        if ans == "q":
            break
        balance+=spin(balance)

    print(f"You left with ₹ {balance}")

__main__()
