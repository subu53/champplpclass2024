""" WK 3 Assignment
Create a function named calculate_discount(price, discount_percent)
that calculates the final price after applying a discount.
The function should take the original price (price) and the discount
percentage (discount_percent) as parameters. If the discount is 20%
or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the
original price of an item and the discount percentage.
Print the final price after applying the discount,
or if no discount was applied, print the original price. """


def calculate_discount(price, discount_percent):
     if discount_percent > 20:
         return price  # No discount applied
     else:
         allowed_discount = min(discount_percent, 20)
         final_price = price - (price * (allowed_discount / 100))
         return final_price
# Get user input
original_price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate final price and message
final_price = calculate_discount(original_price, discount_percent)

# Print the results
print(f"Original price: Kshs {original_price:.2f}")
print(f"Discount: {discount_percent}%")
print(f"Final price: Kshs {final_price:.2f}")
