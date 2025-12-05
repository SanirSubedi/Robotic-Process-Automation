from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
from RPA.PDF import PDF
from datetime import datetime
from fpdf import FPDF

# Corrected category mapping
Corrected_CATEGORY = {
    "food": "Food",
    "utilities": "Utilities",
    "other": "Other",
    "entert": "Entertainment",
    "utilit": "Utilities",
    "othr": "Other",
    "shopping": "Shopping",
    "shop": "Shopping",
    "shoping": "Shopping",
    "oter": "Other",
    "trasport": "Transportation",
    "tranport": "Transportation",
    "transport": "Transportation"
}

expenses = []  # Global list to store expenses

@task
def final_project():
    """Main function to run the workflow."""
    download_file()
    import_file()
    open_website()
    fill_and_submit_form()
    capture_summary()
    create_pdf_summary()


def download_file():
    """Download the expense file from a URL."""
    http = HTTP()
    http.download(
        url="https://fspacheco.github.io/rpa-challenge/assets/list-expenses.txt",
        target_file="list-expenses.txt",
        overwrite=True
    )


def import_file():
    """Read and process the downloaded expense file."""
    global expenses
    year = datetime.now().year

    with open("list-expenses.txt", "r") as file:
        for line in file.readlines():
            try:
                date, description, amount, category = line.strip().split()
                amount = amount.replace(",", ".")  # Ensure consistent decimal format
                new_category = Corrected_CATEGORY.get(category.lower(), category)

                # Convert date format
                day, month = map(int, date.split("/"))
                #map() function is used to apply a given function to every item of an iterable,
                #Splits the date string (e.g., 27/9) into parts based on the / separator.
                new_date = f"{year}-{month:02d}-{day:02d}"  
                '''0: to start the day with 07 not only 7,
                           2: 2 character width,
                           d: decimal character'''

                expenses.append({
                    "TransactionDate": new_date,
                    "Item": description,
                    "Cost": float(amount),
                    "Category": new_category
                })
            except Exception as e:
                print(f"Error processing line: {line}. Error: {e}")


def open_website():
    """Open the expense tracker website."""
    browser.configure(slowmo=100)
    browser.goto("https://fspacheco.github.io/rpa-challenge/expense-tracker.html")


def fill_and_submit_form():
    """Fill the web form with expense details and submit."""
    page = browser.page()
    for expense in expenses:
        page.fill("#description", expense["Item"])
        page.fill("#amount", str(expense["Cost"]))
        page.fill("#date", expense["TransactionDate"])
        page.select_option("#category", expense["Category"])
        page.press("#expenseForm", "Enter")

def capture_summary():
    """Take a screenshot of the summary section."""
    page = browser.page()
    page.screenshot(path="output/summary_image.png")

def create_pdf_summary():
    """Generate a PDF report of expenses, including the highest expense, shop with the most spending, and the highest spending category"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Expense Report", ln=True, align="C")
    pdf.ln(10)

    # Add details to the PDF
    for expense in expenses:
        pdf.cell(0, 10, txt=f"{expense['TransactionDate']} - {expense['Item']} - {expense['Category']} - ${expense['Cost']:.2f}", ln=True)

    # Calculate the highest expense
    highest_expense = max(expenses, key=lambda x: x["Cost"])

    # Calculate total spending by shop/company
    shop_totals = {}
    for expense in expenses:
        shop = expense['Item']  
        shop_totals[shop] = shop_totals.get(shop, 0) + expense['Cost']

    # Find the shop with the highest total spending
    top_shop = max(shop_totals, key=shop_totals.get)

    # Calculate total spending by category
    category_totals = {}
    for expense in expenses:
        category = expense['Category']
        category_totals[category] = category_totals.get(category, 0) + expense['Cost']

    # Find the category with the highest total spending
    top_category = max(category_totals, key=category_totals.get)

    pdf.ln(10)
    pdf.cell(0, 10, txt="Report Summary:", ln=True)
    pdf.cell(0, 10, txt=f"Highest Expense: {highest_expense['Item']} - {highest_expense['Category']} - ${highest_expense['Cost']:.2f}", ln=True)
    pdf.cell(0, 10, txt=f"Date of Highest Expense: {highest_expense['TransactionDate']}", ln=True)
    pdf.cell(0, 10, txt=f"Shop-Company with Most Spending: {top_shop} (${shop_totals[top_shop]:.2f})", ln=True)
    pdf.cell(0, 10, txt=f"Category with Most Spending: {top_category} (${category_totals[top_category]:.2f})", ln=True)

    # Save the PDF
    pdf.output("output/summary_report.pdf")
