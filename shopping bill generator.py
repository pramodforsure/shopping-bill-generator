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
