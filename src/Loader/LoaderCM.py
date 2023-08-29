from src.Models.AccountLine import AccountLine
import pandas as pd

def load_excel_data(path: str) -> list[AccountLine]:
    """
    Load data from an Excel file into a list of AccountLine objects.

    :param path: The path to the Excel file.
    :return: A list of AccountLine objects representing the data from the Excel file.
    """
    # Load the Excel file into a DataFrame
    data_frame = pd.read_excel(path, sheet_name=1, skiprows=4)

    # Create a list to store AccountLine objects
    account_lines = []

    # Populate the list with AccountLine objects corresponding to the rows in the spreadsheet
    for index, row in data_frame.iterrows():
        date = row['Date']
        value = row['Valeur']
        label = row['Libellé']
        debit = row['Débit']
        credit = row['Crédit']
        balance = row['Solde']
        currency = row['Dev']
        bank = "Crédit Mutuel"
        
        if pd.isnull(date):
            break

        # Create an AccountLine object and add it to the list
        account_line = AccountLine(date, value, label, debit, credit, balance, currency, bank)
        account_lines.append(account_line)

    # Display AccountLine objects
    for account_line in account_lines:
        print(account_line)
        print("================================")

    return account_lines
