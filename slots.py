import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3

symbol_count = {
    "E": 8,
    "D": 5,
    "C": 3,
    "B": 2,
    "A": 1
}

symbol_values = {
    "A": 144,
    "B": 89,
    "C": 55,
    "D": 34,
    "E": 21
}

def check_winnigs(columns, lines, bet, values):
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def roll_slots():
    pass


def print_slotmachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
        print()


def deposit():
    """collects user input"""
    while True:
        amount = input("Make deposit:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("0 is not enough")
        else:
            print("Enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter amount between 1 and {MAX_LINES}")
        else:
            print("Enter a number")
    return lines

def get_bet():
    while True:
        amount = input("Make bet on each line on amount:")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Enter a number.")
    return amount



def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You don't have enough money to bet. Balance:" + balance)
        else:
            break
    print(f"You are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}")
    while True:
        spin = input("Do You want to spin?")
        if balance <= 0:
            print("Bankrupt!")
            break
        if 'n' in spin:
            break
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slotmachine(slots)
        balance -= total_bet
        

main()