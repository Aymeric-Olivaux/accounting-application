import os
import openpyxl
from datetime import datetime
from src.Models.AccountLine import AccountLine

def create_excel_file() -> openpyxl.Workbook:
    """
    Create a new Excel file with a given filename and return the workbook.

    :param file_name: The desired filename for the Excel file.
    :return: An openpyxl.Workbook object representing the Excel file.
    """
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    headers = ["Date", "Value", "Label", "Category", "Debit", "Credit", "Balance", "Currency", "Bank"]
    sheet.append(headers)

    return workbook

def append_lines_to_excel(workbook: openpyxl.Workbook, account_lines: list[AccountLine]) -> openpyxl.Workbook:
    """
    Append a list of AccountLine objects to the given Excel workbook.

    :param workbook: The openpyxl.Workbook object representing the Excel file.
    :param account_lines: A list of AccountLine objects to be added to the workbook.
    :return: The updated openpyxl.Workbook object.
    """
    sheet = workbook.active

    for account_line in account_lines:
        
        row_data = [
            account_line.date.strftime("%d/%m/%Y"),  # Formatted date
            account_line.value.strftime("%d/%m/%Y"),  # Formatted value
            account_line.label,
            account_line.category,
            account_line.debit,
            account_line.credit,
            account_line.balance,
            account_line.currency,
            account_line.bank,
        ]
        sheet.append(row_data)
        
    return workbook


def save_excel_file(workbook: openpyxl.Workbook, file_name: str) -> None:
    """
    Save the Excel workbook to a file.

    :param workbook: The openpyxl.Workbook object representing the Excel file.
    :param file_name: The filename to save the Excel file as.
    """
    if os.path.exists(file_name):
        index = 1
        while os.path.exists(f"{file_name}_{index}.xlsx"):
            index += 1
        file_name = f"{file_name}_{index}.xlsx"

    workbook.save(file_name)
