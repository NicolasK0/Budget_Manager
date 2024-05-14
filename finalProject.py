import csv
import os

class BudgetManager:
    def __init__(self):
        self.transactions = []

    def load_data_from_file(self, file_path):
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    self.transactions = self.parse_csv(file)
                print("Data loaded successfully.")
            else:
                print("File not found.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_data_to_file(self, file_path):
        try:
            with open(file_path, 'w', newline='') as file:
                self.write_csv(file)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_transaction(self, date, description, amount):
        self.transactions.append(Transaction(date, description, amount))

    def display_transactions(self):
        if not self.transactions:
            print("No transactions to display.")
        else:
            for transaction in self.transactions:
                print(f"{transaction.date} - {transaction.description} - ${transaction.amount}")

    def parse_csv(self, file):
        reader = csv.reader(file)
        next(reader, None)  # Skip header row
        return [Transaction(*row) for row in reader]

    def write_csv(self, file):
        writer = csv.writer(file)
        writer.writerow(['Date', 'Description', 'Amount'])
        for transaction in self.transactions:
            writer.writerow([transaction.date, transaction.description, transaction.amount])

class Transaction:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

# Example usage
if __name__ == "__main__":
    try:
        input_file_path = 'transactions.csv'
        output_file_path = 'output.csv'

        budget_manager = BudgetManager()

        # Load data from a file
        budget_manager.load_data_from_file(input_file_path)

        # Add new transactions
        budget_manager.add_transaction('2023-01-01', 'Groceries', 50.00)
        budget_manager.add_transaction('2023-01-02', 'Dinner', 30.00)

        # Display transactions
        budget_manager.display_transactions()

        # Save data to a file
        budget_manager.save_data_to_file(output_file_path)

    except Exception as e:
        print(f"An error occurred: {e}")
