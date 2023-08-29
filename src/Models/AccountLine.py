class AccountLine:
    def __init__(self, date: str, value: str, label: str, debit: str, credit: str, balance: str, currency: str, bank: str):
        """
        Initialize an AccountLine object.

        :param date: The date of the account entry.
        :param value: The value associated with the account entry.
        :param label: The label or description of the account entry.
        :param debit: The debit amount for the account entry.
        :param credit: The credit amount for the account entry.
        :param balance: The balance after the account entry.
        :param currency: The currency of the account entry.
        :param bank: The bank associated with the account entry.
        """
        self.date = date
        self.value = value
        self.label = label
        self.debit = debit
        self.credit = credit
        self.balance = balance
        self.currency = currency
        self.bank = bank

        self.category = "null"

    def __str__(self):
        """
        Return a human-readable string representation of the AccountLine object.

        :return: A formatted string with account entry details.
        """
        return (
            f"Date: {self.date}\n"
            f"Value: {self.value}\n"
            f"Label: {self.label}\n"
            f"Category: {self.category}\n"
            f"Debit: {self.debit}\n"
            f"Credit: {self.credit}\n"
            f"Balance: {self.balance}\n"
            f"Currency: {self.currency}\n"
            f"Bank: {self.bank}\n"
        )
