# Robotic Process Automation (RPA) Projects

A comprehensive collection of automation projects demonstrating proficiency in RPA tools, web scraping, data processing, and workflow automation using industry-standard frameworks.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![RPA](https://img.shields.io/badge/RPA-Robocorp-green.svg)
![UIPath](https://img.shields.io/badge/UIPath-Certified-orange.svg)

## Overview

This repository showcases a progression of RPA projects from basic web automation to complex data processing workflows. All projects were developed as part of the Robotics Process Automation course at HAMK University of Applied Sciences, demonstrating practical application of automation principles in real-world scenarios.

## Technologies & Tools

- **RPA Platforms:** Robocorp (Sema4.ai), UIPath
- **Programming:** Python 3.9+
- **Libraries & Frameworks:**
  - `robocorp.browser` - Web automation
  - `RPA.Excel.Files` - Excel file manipulation
  - `RPA.PDF` - PDF generation and processing
  - `openpyxl` - Advanced Excel operations
  - `FPDF` - Custom PDF creation
- **Web Technologies:** HTML/CSS selectors, XPath
- **Data Processing:** Excel, PDF, text file parsing

## Projects

### 1. Library Search Automation (UIPath)
**Platform:** UIPath Studio

Automated library catalog search on HAMK Finna platform with intelligent navigation and search capabilities.

**Key Features:**
- Browser automation with multi-step workflow
- Dynamic element interaction (language selection, search bar)
- Configurable wait times for page loading
- Cookie handling and form submission

**Skills Demonstrated:**
- UIPath workflow design
- Web element identification
- Timing optimization

**View Screenshots**
- [Step1](img/Step-1.png)
- [Step2](img/Step-2.png)
- [Step3](img/Step-3.png)
---

### 2. Wikipedia Web Scraper (Robocorp)
**Platform:** Robocorp (Sema4.ai)

Automated Wikipedia search and screenshot capture using Python-based RPA framework.

**Technical Implementation:**
```python
@task
def open_page():
    page = browser.goto("https://www.wikipedia.org/")
    page.locator("#searchInput").fill("kathmandu")
    page.locator(".svg-search-icon").wait_for()
    page.locator(".pure-button").click()
    page.keyboard.press("Enter")
    browser.screenshot()
```

**Key Features:**
- Direct Python coding with Robocorp framework
- CSS selector-based element targeting
- Automated screenshot capture
- Minimal-task architecture

**Skills Demonstrated:**
- Python decorators (`@task`)
- Browser automation library
- Web element locators
- Screenshot functionality

[View Code Screenshot](img/automation_website.png)

---

### 3. Music Collection Form Automation
**Platform:** Robocorp | **Complexity:** Intermediate

Automated form-filling workflow integrating Excel data input with web forms, including authentication and data export.

**Workflow:**
1. Download Excel file from remote URL
2. Authenticate with credentials
3. Parse Excel data (Artist, Album, Year, Format, Condition)
4. Fill web form iteratively
5. Capture summary screenshot
6. Export results as PDF

**Technical Highlights:**
- HTTP file download automation
- Excel worksheet parsing with header detection
- Dynamic form field mapping
- Select dropdown automation
- HTML to PDF conversion

**Code Architecture:**
```python
def fill_and_submit_actor_form(music_rep):
    page = browser.page()
    page.fill("#artist", music_rep["Artist"])
    page.fill("#album", music_rep["Album"])
    page.fill("#year", str(music_rep["Release Year"]))
    page.select_option("#format", music_rep["Format"])
    page.select_option("#condition", music_rep["Condition"])
    page.click("#addToCollection")
```

**Skills Demonstrated:**
- Multi-step workflow orchestration
- Data transformation (Excel → Web Form)
- Authentication handling
- PDF generation from HTML

[View Full Code](src/music_collection_automation.py)

**View Result**
- [ollection of Data](img/CollectionOFData)
- [ResultProof1](img/ResultProof1.png)
- [ResultProof2](img/ResultProof2.png) 



---

### 4. Bookstore Data Extraction & Analysis
**Platform:** Robocorp | **Complexity:** Advanced

Comprehensive web scraping project with data validation, Excel export, and automated testing capabilities.

**Project Components:**

#### Task 1: English Bookstore Data Extraction
- Scraped book titles and prices from e-commerce site
- Dynamic data collection using CSS locators
- Excel export with formatting (column width, headers)
- Price data type conversion (string → float)

#### Task 2: Finnish Bookstore Data Extraction
- Multi-language support (Finnish characters: €, Ä, Ö)
- Currency symbol handling
- Duplicate implementation for comparison

#### Task 3: Price Analysis & Highlighting
- Identified minimum price from dataset
- Applied conditional formatting using `openpyxl`
- Visual highlighting with color fills

**Implementation:**
```python
def highlight_cheapest_book():
    workbook = load_workbook("sanir_book_store.xlsx")
    sheet = workbook["books"]
    
    min_price = float('inf')
    min_price_cell = None
    
    for row in sheet.iter_rows(min_row=2, min_col=2, max_col=2):
        for cell in row:
            if cell.value < min_price:
                min_price = cell.value
                min_price_cell = cell
    
    if min_price_cell:
        fill = PatternFill(start_color="FFD580", end_color="FFD580", fill_type="solid")
        min_price_cell.fill = fill
```

#### Task 4: E-commerce Functionality Testing
Automated testing suite validating:
- **Cart System:** Item addition verification
- **Sorting Functionality:** Price order validation
- **Search Feature:** Query result accuracy

**Test Implementation:**
```python
def test_item_by_price():
    page = browser.page()
    prices = page.locator("span.hinta").all_text_contents()
    prices = [float(price.replace("$", "")) for price in prices]
    sorted_prices = sorted(prices)
    
    assert prices == sorted_prices, "Prices not sorted correctly"
```

**Skills Demonstrated:**
- Advanced web scraping techniques
- Data cleaning and transformation
- Excel automation with styling
- Automated testing implementation
- Price comparison algorithms
- String manipulation and parsing

[View Code](src/bookstore_automation.py) | [ Outputs](img/Output_result.png)

---

### 5. Expense Tracker Automation (Final Project)
**Platform:** Robocorp | **Complexity:** Expert Level

End-to-end automation system for expense management with advanced data processing, error correction, and comprehensive reporting.

**System Architecture:**

```
Text File → Download → Parse → Correct Errors → Fill Form → Export PDF → Generate Report
```

**Key Challenges Solved:**

1. **Data Cleaning & Error Correction**
   - Implemented fuzzy matching for category names
   - Dictionary-based typo correction
   - Handled inconsistent formatting

```python
Corrected_CATEGORY = {
    "food": "Food",
    "entert": "Entertainment",
    "utilit": "Utilities",
    "shoping": "Shopping",
    "trasport": "Transportation"
}
```

2. **Date Format Transformation**
   - Parsed DD/MM format from text file
   - Converted to ISO format (YYYY-MM-DD)
   - Dynamic year insertion

```python
day, month = map(int, date.split("/"))
new_date = f"{year}-{month:02d}-{day:02d}"
```

3. **Decimal Format Handling**
   - Converted comma decimals to period decimals
   - String to float conversion with validation

4. **Advanced PDF Generation**
   - Custom PDF creation using FPDF
   - Multi-section report structure
   - Dynamic content insertion
   - Statistical analysis integration

**Report Features:**
- Complete expense history
- Highest single expense identification
- Top spending category analysis
- Shop/company spending breakdown
- Visual summary with charts

**Statistical Analysis Implementation:**
```python
# Highest expense
highest_expense = max(expenses, key=lambda x: x["Cost"])

# Top spending shop
shop_totals = {}
for expense in expenses:
    shop_totals[expense['Item']] = shop_totals.get(expense['Item'], 0) + expense['Cost']
top_shop = max(shop_totals, key=shop_totals.get)

# Top spending category
category_totals = {}
for expense in expenses:
    category_totals[expense['Category']] = category_totals.get(expense['Category'], 0) + expense['Cost']
top_category = max(category_totals, key=category_totals.get)
```

**Technical Achievements:**
- File I/O operations with error handling
- Complex data transformations
- Form automation with dynamic inputs
- PDF generation with calculations
- Statistical data analysis
- Report summarization

**Problem-Solving Journey:**
During development, multiple challenges were encountered:
- Date format incompatibility with web forms
- HTML element identification for form submission
- PDF text insertion complexity
- Dynamic content generation

Solutions involved iterative debugging, HTML inspection, and integration of advanced FPDF features for custom report generation.

**Skills Demonstrated:**
- End-to-end workflow automation
- Error handling and data validation
- Statistical analysis and reporting
- Complex data transformations
- Custom PDF generation
- Advanced Python programming

[View Full Code](src/expense_tracker_automation.py) | [Sample Output](img/final_project_pdf.png) | [Screenshot](img/summary_image.png)

---

## Technical Skills Demonstrated

### RPA Development
- Workflow design and orchestration
- Multi-step automation pipelines
- Error handling and recovery
- Process optimization

### Web Automation
- Browser control and navigation
- Element identification (CSS, XPath, ID)
- Form filling and submission
- Dynamic content handling
- Screenshot capture

### Data Processing
- Excel file manipulation and formatting
- PDF generation and customization
- Text file parsing
- Data cleaning and transformation
- Statistical analysis

### Python Programming
- Decorators and task management
- List comprehensions and lambda functions
- File I/O operations
- String manipulation
- Dictionary operations
- Object-oriented concepts

### Testing & Quality Assurance
- Automated testing implementation
- Validation and assertion
- Edge case handling
- Debugging and troubleshooting

## Project Progression

**Beginner → Intermediate → Advanced → Expert**

1. **Basic Automation** (UIPath library search)
2. **Web Scraping** (Wikipedia bot)
3. **Data Integration** (Music collection)
4. **Data Extraction** (Bookstore scraping)
5. **Complex Systems** (Expense tracker)

Each project builds upon previous concepts while introducing new challenges and technologies.

## Installation & Setup

### Prerequisites
```bash
# Python 3.9 or higher
python --version

# Robocorp CLI
pip install robocorp

# Required libraries
pip install robocorp-browser RPA-Framework openpyxl fpdf
```

### Running Projects

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rpa-automation-projects.git
cd rpa-automation-projects
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run specific project:
```bash
# Example: Music Collection Automation
cd src
python music_collection_automation.py
```

4. Check output:
```bash
ls output/
```

## Key Learnings

### Automation Best Practices
- Always include wait times for page loads
- Use specific selectors for reliability
- Implement error handling for robustness
- Validate data before processing

### Development Insights
- Iterative debugging is essential
- HTML inspection tools are invaluable
- Test with edge cases early
- Documentation saves time

### Technical Growth
- Progressed from GUI-based tools (UIPath) to code-first approach (Robocorp)
- Developed systematic problem-solving methodology
- Learned to integrate multiple technologies seamlessly
- Gained proficiency in data transformation workflows

## Future Enhancements

- [ ] Implement machine learning for intelligent data categorization
- [ ] Add real-time notification system
- [ ] Develop dashboard for expense visualization
- [ ] Integrate with cloud storage (Google Drive, Dropbox)
- [ ] Create REST API for remote access
- [ ] Add multi-user support
- [ ] Implement scheduled automation triggers

## Certifications

- Robocorp Automation Certification Level I (Completed)

## Author

**Sanir Subedi**  
ICT Robotics Student | HAMK University of Applied Sciences

- GitHub: [@Sanir04](https://github.com/Sanir04)
- Email: Sanir.Subedi@student.hamk.fi / sanirsubedi@gmail.com


## Collaborators

Special thanks to my lab partner:
- **Achal Thapa** - [@AchalThapa](https://github.com/AchalThapa) - Collaborative work on Projects 2-5

## References & Resources

- [Robocorp Documentation](https://robocorp.com/docs)
- [RPA Framework](https://rpaframework.org/)
- [UIPath Academy](https://academy.uipath.com/)
- HAMK Robotics Process Automation Course Materials

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Academic Note:** These projects were completed as coursework at HAMK University of Applied Sciences (October - December 2024) and are shared for educational and portfolio purposes.

---

**Last Updated:** December 2024  
**Course:** Robotics Process Automation  
**Program:** ICT Robotics  
**Institution:** HAMK University of Applied Sciences
