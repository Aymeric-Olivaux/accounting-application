from src.Loader.loaderCM import *
from src.Tools.Excel import *

def main():
    """
    Main function to load and process account line data from an Excel file.
    """
    # Path to the Excel file
    path = r'C:\Users\aymer\Downloads\comptes.xlsx'

    # Load account line data using the loaderCM module
    account_lines_cm = load_excel_data(path)

    file_name = r'C:\Users\aymer\OneDrive\BUREAU\financial_data.xlsx'

    workbook = create_excel_file()
    append_lines_to_excel(workbook, account_lines_cm)
    save_excel_file(workbook, file_name)

if __name__ == "__main__":
    main()
