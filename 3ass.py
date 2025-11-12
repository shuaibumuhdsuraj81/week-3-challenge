# discount

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        print(f'final price: {final_price}')
    else:
        print(f'normal price: {price}')
print(calculate_discount(1500, 20))

#prompting the user
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display final price
final_price = calculate_discount(price, discount_percent)

print("The final price after discount is:", final_price)