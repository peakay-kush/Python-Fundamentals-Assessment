# Discount Program
# Ask for product details
product_name = input("Enter the product name: ")
price = float(input("Enter the product price: "))

# Apply discount based on price
if price > 10000:
    discounted_price = price - (price * 0.20)
elif 5000 <= price <= 10000:
    discounted_price = price - (price * 0.10)
else:
    discounted_price = price  # No discount

# Display the result
print(f"The {product_name} now costs {discounted_price} KES after discount.")

