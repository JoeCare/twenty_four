
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

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
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}")
    



main()