class User:
    account_number = 1000
    users = []
    bank_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True

    def __init__(self, name, email, address, account_type):
        User.account_number += 1
        self.account_number = User.account_number
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposited {amount}')
        User.bank_balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdrew {amount}')
            User.bank_balance -= amount
        else:
            print('Withdrawal amount exceeded')

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if User.loan_feature_enabled and self.loan_taken < 2:
            self.loan_taken += 1
            self.balance += amount
            self.transaction_history.append(f'Loan received: {amount}')
            User.total_loan_amount += amount
        else:
            print('Loan not available')

    def transfer(self, target_user, amount):
        if target_user is None:
            print('Account does not exist')
        elif amount <= self.balance:
            self.withdraw(amount)
            target_user.deposit(amount)
        else:
            print('Insufficient funds')

class Admin:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    @staticmethod
    def create_account():
        name = input("Enter user's name: ")
        email = input("Enter user's email: ")
        address = input("Enter user's address: ")
        account_type = input('Enter account type (Savings/Current): ')
        if account_type not in ['Savings', 'Current']:
            print('Invalid account type')
            return
        new_user = User(name, email, address, account_type)
        User.users.append(new_user)
        print(f'Account created successfully. Account number: {new_user.account_number}')

    @staticmethod
    def delete_user_account():
        user_account_number = int(input('Enter the account number to delete: '))
        for user in User.users:
            if user.account_number == user_account_number:
                User.users.remove(user)
                print(f'Account {user_account_number} deleted successfully.')
                return
        print('Account not found')

    @staticmethod
    def see_all_user_accounts():
        for user in User.users:
            print(f'Account Number: {user.account_number}, Name: {user.name}, Balance: {user.balance}')

    @staticmethod
    def check_total_bank_balance():
        return User.bank_balance

    @staticmethod
    def check_total_loan_amount():
        return User.total_loan_amount

    @staticmethod
    def toggle_loan_feature():
        User.loan_feature_enabled = not User.loan_feature_enabled

def main():
    admin = Admin(user_id='admin', password='password')
    while True:
        print('1. Users')
        print('2. Admin')
        print('3. Exit')
        user_input = input('Enter your choice: ')
        if user_input == "1":
            account_number = int(input('Enter your account number: '))
            
            user = next((u for u in User.users if u.account_number == account_number), None)
            if user:
                while True:
                    print('  User Menu:')
                    print('1. Deposit')
                    print('2. Withdraw')
                    print('3. Check Balance')
                    print('4. Transaction History')
                    print('5. Take Loan')
                    print('6. Transfer Money')
                    print('7. Exit User Menu')
                    choice = input('Enter your choice: ')
                    if choice == '1':
                        amount = float(input('Enter the amount to deposit: '))
                        user.deposit(amount)
                    elif choice == '2':
                        amount = float(input('Enter the amount to withdraw: '))
                        user.withdraw(amount)
                    elif choice == "3":
                        print(f'Available balance: {user.check_balance()}')
                    elif choice == '4':
                        print('Transaction History:')
                        for transaction in user.check_transaction_history():
                            print(transaction)
                    elif choice == '5':
                        amount = float(input('Enter the loan amount: '))
                        user.take_loan(amount)
                    elif choice == '6':
                        target_account = int(input('Enter the target account number: '))
                        target_user = next((u for u in User.users if u.account_number == target_account), None)
                        user.transfer(target_user, amount)
                    elif choice == '7':
                        break
                    else:
                        print('Invalid choice')
            else:
                print('Invalid user account')

        elif user_input == '2':
            print("Default user id 'admin' and Default password 'password' ")
            admin_user_id = input('Enter admin user ID: ')
            admin_password = input('Enter admin password: ')
            if admin_user_id == admin.user_id and admin_password == admin.password:
                while True:
                    print('   Admin Menu:')
                    print('1. Create Account')
                    print('2. Delete User Account')
                    print('3. See All User Accounts')
                    print('4. Check Total Bank Balance')
                    print('5. Check Total Loan Amount')
                    print('6. Toggle Loan Feature')
                    print('7. Exit Admin Menu')
                    admin_choice = input('Enter your choice: ')
                    if admin_choice == '1':
                        admin.create_account()
                    elif admin_choice == '2':
                        admin.delete_user_account()
                    elif admin_choice == '3':
                        admin.see_all_user_accounts()
                    elif admin_choice == '4':
                        print(f'Total Bank Balance: {admin.check_total_bank_balance()}')
                    elif admin_choice == '5':
                        print(f'Total Loan Amount: {admin.check_total_loan_amount()}')
                    elif admin_choice == '6':
                        admin.toggle_loan_feature()
                        print(f"Loan feature {'enabled' if User.loan_feature_enabled else 'disabled'}")
                    elif admin_choice == '7':
                        break
                    else:
                        print('Invalid choice')
            else:
                print('Invalid admin credentials')
        elif user_input == '3':
            break
        else:
            print("Invalid input. Please enter 'user' or 'admin'.")

if __name__ == '__main__':
    main()
