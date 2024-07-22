from datetime import datetime

def map_category(category):
    """Convert category short form to full form."""
    if category.upper() in ['C', 'CREDIT']:
        return 'Credit'
    elif category.upper() in ['D', 'DEBIT']:
        return 'Debit'
    else:
        return None

def record_transaction(amount, category, description):
    full_category = map_category(category)
    if full_category is None:
        print('Invalid category. Please enter "C" for Credit or "D" for Debit.')
        return
    with open('transactions.txt', 'a') as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{amount},{full_category},{description}\n")

def display_summary():
    total_credit = 0
    total_debit = 0
    with open('transactions.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            amount = float(parts[1])
            if parts[2] == 'Credit':
                total_credit += amount
            elif parts[2] == 'Debit':
                total_debit += amount
    net_balance = total_credit - total_debit
    print(f'Total Credit: {total_credit}')
    print(f'Total Debit: {total_debit}')
    print(f'Net Balance: {net_balance}')

def display_transactions():
    with open('transactions.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            print(f'Date: {parts[0]}, Amount: {parts[1]}, Category: {parts[2]}, Description: {parts[3]}')

def main():
    while True:
        print('\n1. Record Transaction')
        print('2. Display Summary')
        print('3. Display Transactions')
        print('4. Exit')
        choice = input('Select an option: ')
        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
                category = input('Enter category (C for Credit / D for Debit): ')
                description = input('Enter description: ')
                record_transaction(amount, category, description)
            except ValueError:
                print('Invalid amount. Please enter a number.')
        elif choice == '2':
            display_summary()
        elif choice == '3':
            display_transactions()
        elif choice == '4':
            break
        else:
            print('Invalid selection, please try again.')

if __name__ == '__main__':
    main()
