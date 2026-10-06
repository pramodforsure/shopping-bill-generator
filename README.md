 Shopping Bill Generator

A beginner-friendly Python program that calculates the total cost of a product, applies a discount when the purchase reaches ₹1000 or more, and displays the final amount.

 About the Project

I am a freshman undergraduate learning Python. This is a beginner Python practice project focused on user input, variables, arithmetic operations, and conditional statements.

 What the Program Does

The program:

1. Takes the product name.
2. Takes the product price.
3. Takes the quantity.
4. Calculates the total price.
5. Applies a 10% discount when the total is ₹1000 or more.
6. Calculates the final amount.
7. Displays the bill details.

 Discount Rule

- **Total ≥ ₹1000:** 10% discount
- **Total < ₹1000:** No discount

 Concepts Used

- `input()`
- `int()`
- Variables
- Multiplication
- Subtraction
- `if / else`
- Comparison operators
- f-strings

 Code

```python
product_name = input("Enter product name: ")
product_price = int(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = product_price * quantity

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

print(f"Product: {product_name}")
print(f"Price: {product_price}")
print(f"quantity: {quantity}")
print(f"total: {total}")
print(f"discount: {discount}")
print(f"final amount: {final_amount}")
Example
Enter product name: Keyboard
Enter product price: 600
Enter quantity: 2

Product: Keyboard
Price: 600
quantity: 2
total: 1200
discount: 120.0
final amount: 1080.0
Requirements
Python 3.x
No external libraries
How to Run

Run the program from a terminal:
python "shopping bill generator.py"
Then enter the requested product details.

Learning Status

Level: Beginner
Project Type: Python Practice Project
Focus: Input, arithmetic operations, conditions, and formatted output

Future Improvements
Allow multiple products in one bill.
Add customer details.
Format amounts to two decimal places.
Add different discount levels.
Add tax/GST calculation.
Use functions to organize the billing logic.
Store multiple products using lists or dictionaries.
Author

A freshman undergraduate learning Python and developing programming fundamentals through hands-on projects.
