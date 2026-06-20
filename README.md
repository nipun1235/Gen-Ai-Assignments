# Assignment 2: Python - Control Flow (Conditionals & Loops)

## Student Information

- Name: Nipun Bhardwaj
- Course: B.Tech (Information Technology)
- Assignment: Assignment 2 - Python Control Flow (Conditionals & Loops)

---

## Assignment Overview

This assignment focuses on Python control flow concepts including:

- if / elif / else statements
- for loops
- while loops
- break statement
- continue statement
- Lists and basic arithmetic operations

All solutions are implemented in separate Jupyter Notebook files as required.

---

## Files Included

### 1. conditional_ass2.ipynb

Contains solutions for:

#### Task 1: Discount Rules
- Read order amount from user
- Apply discounts based on order value
- Display final amount
- Handle invalid input

---

### 2. forloop_ass2.ipynb

Contains solutions for:

#### Task 2: Process Multiple Orders
- Apply discount rules to multiple orders
- Display summary table
- Calculate total revenue
- Count orders receiving discounts

---

### 3. whileloop_ass2.ipynb

Contains solutions for:

#### Task 3: User Menu
- Implement menu using while loop
- Add order amounts
- Display discounted orders
- Use break and continue

---

### 4. loopcontrol_ass2.ipynb

Contains solutions for:

#### Task 5: Loop Control with Conditions
- Process daily sales data
- Skip no-sale days using continue
- Stop processing corrupted data using break
- Calculate running total and final sales total

---

## Concepts Used

- Variables
- Input and Output
- Arithmetic Operators
- Conditional Statements
- Lists
- For Loop
- While Loop
- Break Statement
- Continue Statement

---

## How to Run

1. Open Jupyter Notebook or VS Code.
2. Open the required notebook file.
3. Run cells sequentially.
4. Verify outputs for each task.

---

## Author

Nipun Bhardwaj# Assignment 2: Python - Control Flow (Conditionals & Loops)

## Student Information

- Name: Nipun Bhardwaj
- Course: Gen AI Tutedude
- Assignment: Assignment 2 - Python Control Flow (Conditionals & Loops)

---

## Assignment Overview

This assignment focuses on Python control flow concepts including:

- if / elif / else statements
- for loops
- while loops
- break statement
- continue statement
- Lists and basic arithmetic operations

All solutions are implemented in separate Jupyter Notebook files as required.

---

## Files Included

### 1. conditional_ass2.ipynb

Contains solutions for:

#### Task 1: Discount Rules
- Read order amount from user
- Apply discounts based on order value
- Display final amount
- Handle invalid input

---

### 2. forloop_ass2.ipynb

Contains solutions for:

#### Task 2: Process Multiple Orders
- Apply discount rules to multiple orders
- Display summary table
- Calculate total revenue
- Count orders receiving discounts

---

### 3. whileloop_ass2.ipynb

Contains solutions for:

#### Task 3: User Menu
- Implement menu using while loop
- Add order amounts
- Display discounted orders
- Use break and continue

---

### 4. loopcontrol_ass2.ipynb

Contains solutions for:

#### Task 4: Loop Control with Conditions
- Process daily sales data
- Skip no-sale days using continue
- Stop processing corrupted data using break
- Calculate running total and final sales total

---

## Concepts Used

- Variables
- Input and Output
- Arithmetic Operators
- Conditional Statements
- Lists
- For Loop
- While Loop
- Break Statement
- Continue Statement

---
## Assignment 3: Functions

Tasks Completed

- Task 1: Created "apply_discount()" function using parameters and default arguments.
- Task 2: Implemented recursive "factorial()" function with handling for 0, 1, and negative numbers.
- Task 3: Created GST calculator using lambda functions and calculated final price after GST and discount.
- Task 4: Applied GST to a list of prices using "map()".
- Task 5: Filtered expensive and affordable products using "filter()".
- Task 6: Created "process_prices()" function using both "map()" and "filter()" to generate discounted and filtered price lists.
- Task 7: Implemented a menu-driven program using functions and loops:
  - Add Price
  - Show Average Price
  - Show Highest Price
  - Quit

Concepts Used

- Functions
- Parameters and Arguments
- Default Arguments
- Recursion
- Lambda Functions
- map()
- filter()
- Lists
- Loops
- Conditional Statements

## How to Run

1. Open Jupyter Notebook or VS Code.
2. Open the required notebook file.
3. Run cells sequentially.
4. Verify outputs for each task.

---
## Assignment 4: File Handling

### Files Created
- sales_data.txt
- products.txt
- discount_report.txt

### Topics Covered
- File Creation
- File Reading
- File Writing
- File Appending
- read()
- readline()
- readlines()
- File Existence Check
- Dictionary Data Export
- Basic Report Generation

### Tasks Completed

#### Task 1: Write Sales Records to a File
- Created a list of sales amounts.
- Wrote sales values to `sales_data.txt`.
- Reopened the file and displayed its contents.

#### Task 2: Read File in Different Ways
- Read complete file using `read()`.
- Read first line using `readline()`.
- Read all lines using `readlines()`.
- Converted file data into a list of integers.

#### Task 3: Append New Sales
- Appended additional sales values to `sales_data.txt`.
- Printed the updated file contents.
- Counted total records after appending.

#### Task 4: Generate Summary Report
- Read sales data from file.
- Converted values to integers.
- Calculated:
  - Total Sales
  - Highest Sale
  - Lowest Sale
  - Average Sale

#### Task 5: Create Product Info File
- Collected product names and prices from user input.
- Stored product data in `products.txt`.
- Displayed formatted product records from the file.

#### Task 6: Read File Safely
- Accepted filename from the user.
- Checked file existence using `os.path.exists()`.
- Displayed file contents if found.
- Displayed an error message if file was missing.

#### Task 7: Mini Project - Export Discounted Prices
- Created a product-price dictionary.
- Accepted discount percentage from the user.
- Calculated discounted prices.
- Exported results to `discount_report.txt`.
- Read and displayed the generated report.

### Concepts Practiced
- File Modes (`r`, `w`, `a`)
- File Handling Operations
- Dictionaries
- Loops
- Conditional Statements
- User Input
- String Formatting
- Basic Data Processing

## Assignment 5: Modules and Packages

### Tasks Completed

#### Task 1: Simple Module (math_utils.py)
Created a module `math_utils.py` with the following functions:
- add(a, b)
- subtract(a, b)
- square(n)

Tested module using:
```python
import math_utils
from math_utils import square
```

---

#### Task 2: String Module (string_utils.py)
Created a module `string_utils.py` with:
- capitalize_words(text)
- reverse_string(text)
- word_count(text)

Imported and tested all functions in main.py.

---

#### Task 3: Simple Package (shop_package)
Created package structure:

```text
shop_package/
│
├── __init__.py
├── discount.py
└── billing.py
```

##### discount.py
Functions:
- apply_discount(price, percent)
- flat_discount(price)

##### billing.py
Functions:
- calculate_total(prices)
- apply_tax(amount)

##### __init__.py
Imported package functions for easier access.

---

#### Task 4: Importing Package in main.py

Used different import styles:

```python
import shop_package.discount as disc

from shop_package.billing import calculate_total
```

Tested package functions:

```python
print(disc.apply_discount(1000, 10))

print(calculate_total([100, 200, 300]))
```

---
### Concepts Practiced
- Creating Python modules
- Importing modules
- Using `import`
- Using `from ... import`
- Creating packages
- Using `__init__.py`
- Importing package modules
- Organizing code into reusable components


# Assignment 6 - Exception Handling

## Task 1: Safe Division Utility
- Took numerator and denominator as user input.
- Used `try-except` to handle:
  - `ValueError` for invalid numeric input.
  - `ZeroDivisionError` when denominator is 0.
- Printed result inside the `else` block when no error occurred.
- Used `finally` block to print:
  - `Operation Complete`

## Task 2: Bill Calculator with Error Handling
- Processed a list of product prices.
- Added only valid positive numeric values to the total.
- Handled:
  - `TypeError` for non-numeric values.
  - Custom `ValueError("Negative price not allowed")` for negative prices.
- Printed running total after processing valid values.
- Skipped invalid entries and continued execution.

## Task 3: Custom Exception - Age Validator
- Created `check_age(age)` function.
- Raised:
  - `ValueError("Age must be between 1 and 120")`
    when age was outside the valid range.
- Took age input from the user.
- Used `try-except` to catch and display the custom exception message.

## Task 4: File Reader with Exception Handling
- Took filename input from the user.
- Attempted to open and read the file.
- Handled:
  - `FileNotFoundError`
  - `PermissionError`
- Printed the first three lines of the file if successful.
- Used `finally` block to print:
  - `File operation attempted`

## Task 5: Safe Shopping Cart
- Created a shopping cart list.
- Accepted prices from the user until `q` was entered.
- Converted input values to float.
- Handled:
  - `ValueError` for invalid inputs.
  - Custom exception for negative prices.
- Stored only valid positive prices.
- Printed:
  - Total Items
  - Total Bill
# OOPs Assignment 7 - Python

This repository contains solutions for Object-Oriented Programming (OOP) tasks in Python.

---

## Task 1: Basic Class & Object Creation

Created a `Product` class with:

### Attributes
- name
- price
- category

### Methods
- `get_info()` → Prints product details
- `apply_discount(percent)` → Returns discounted price

### Concepts Covered
- Class
- Object
- Constructor
- Attributes
- Methods

---

## Task 2: Constructor & Encapsulation

Modified the Product class to implement encapsulation.

### Features
- Private attribute: `__price`
- Getter Method:
  - `get_price()`
- Setter Method:
  - `set_price(new_price)`

### Validation
- Price updates only if new price is greater than 0.

### Concepts Covered
- Encapsulation
- Getter & Setter Methods
- Private Attributes

---

## Task 3: Inheritance (Single-Level)

Created subclass:

### ElectronicProduct(Product)

Additional Attribute:
- warranty_years

Overridden Method:
- `get_info()`

### Concepts Covered
- Inheritance
- Method Overriding
- super()

---

## Task 4: Polymorphism

Created two classes:

- Laptop(Product)
- Mobile(Product)

Both classes override:

```python
get_info()
```

A loop was used to call the same method on different objects.

### Concepts Covered

- Polymorphism
- Method Overriding
- Dynamic Method Dispatch

---

## Task 5: Abstraction

Created an Abstract Base Class:

### Payment

Abstract Method:

```python
process_payment(amount)
```

Derived Classes:

- CreditCardPayment
- UPIPayment

Both implement their own payment processing methods.

### Concepts Covered

- Abstraction
- Abstract Base Classes (ABC)
- Abstract Methods

---

## Task 6: Magic Methods & Operator Overloading

Implemented:

### __str__()

Returns a readable representation of Product objects.

Example:

```python
Product(Laptop, 85000, Electronics)
```

### __add__()

Allows:

```python
product1 + product2
```

Returns combined product price.

### Concepts Covered

- Magic Methods
- Operator Overloading
- __str__
- __add__

---

## Task 7: Mini Project - Inventory Management System

Created two classes:

### Product

Stores:
- Name
- Price
- Category

### Inventory

Methods:
- add_product()
- remove_product()
- show_all_products()
- get_total_value()

### Store

Methods:
- add_new_product()
- show_summary()

### Features

- Add Products
- Remove Products
- Display Products
- Calculate Total Inventory Value
- Product Price Combination using __add__()

### Concepts Covered

- Classes & Objects
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Magic Methods
- Operator Overloading

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

# Streamlit Assignment

## Task 1: Hello World App

### Features
- Displayed a simple message using Streamlit.
- Used `st.write()` to print text on the web page.

### Concepts Used
- Streamlit Installation
- st.write()

---

## Task 2: Price Calculator App

### Features
- Takes product price as input.
- Takes discount percentage using slider.
- Calculates discounted price on button click.
- Displays final price using `st.success()`.
- Shows comparison of original and discounted price.

### Concepts Used
- st.number_input()
- st.slider()
- st.button()
- st.success()
- st.table()

---

## Task 3: Product Form App

### Features
- Accepts product name, category, and price.
- Uses Streamlit sidebar for inputs.
- Displays product details in tabular format.
- Shows success message when product is added.

### Concepts Used
- st.sidebar.text_input()
- st.sidebar.selectbox()
- st.sidebar.number_input()
- st.sidebar.button()
- st.table()

---

## Task 4: Mini Sales Dashboard

### Features
- Displays monthly sales dashboard.
- Select month using dropdown.
- Shows selected month's sales.
- Displays sales data using a bar chart.

### Sales Data

```python
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}
```

### Concepts Used
- Python Dictionary
- st.selectbox()
- st.metric()
- st.bar_chart()

---

## Learning Outcomes

Through these assignments, I learned:

- Streamlit Basics
- User Input Handling
- Sidebar Components
- Tables and Metrics
- Data Visualization
- Building Interactive Web Apps with Python

### Author
Nipun Bhardwaj
