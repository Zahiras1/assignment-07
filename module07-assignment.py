# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
product1 = ("P001", "Smartphone X", 799.99, 10, "Mobile Phones")
product2 = ("P002", "Laptop Pro 15", 1299.99, 5, "Laptops")
product3 = ("P003", "Wireless Earbuds", 149.99, 20, "Audio")
product4 = ("P004", "Gaming Laptop", 1599.99, 3, "Laptops")
product5 = ("P005", "Bluetooth Speaker", 89.99, 15, "Audio")

# TODO 2: Create an inventory list containing all product tuples
inventory = [product1, product2, product3, product4, product5]

# TODO 3: Display all products
print("\nCurrent Inventory:")
print("-" * 60)

for product in inventory:
    print(product)

# TODO 4: Access specific elements
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

print("\n\nAccessing Specific Products:")
print("-" * 60)

print("First Product:", first_product)
print("Last Product:", last_product)
print("Third Product Name:", third_product_name)
print("Second Product Price:", second_price)
print("Second Product Quantity:", second_quantity)

# TODO 5: Use slicing to get subsets
first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)

print("First Three:", first_three)
print("Middle Products:", middle_products)
print("All Except First:", all_except_first)

# TODO 6: Add new products to inventory
product6 = ("P006", "Smartwatch Z", 299.99, 12, "Mobile Phones")
product7 = ("P007", "Noise Cancelling Headphones", 399.99, 6, "Audio")

inventory.append(product6)
inventory.append(product7)

print("\n\nAdding New Products:")
print("-" * 60)

for product in inventory:
    print(product)

# TODO 7: Remove a product
removed_product = inventory.pop(2)

print("\n\nRemoving a Product:")
print("-" * 60)

print("Removed:", removed_product)

for product in inventory:
    print(product)

# TODO 8: Insert a product at a specific position
product8 = ("P008", "Tablet Plus", 499.99, 8, "Mobile Phones")

inventory.insert(1, product8)

print("\n\nInserting a Product:")
print("-" * 60)

for product in inventory:
    print(product)

# REDO TODO 4 and 5
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

# TODO 9: Create category lists
mobile_phones = []
laptops = []
audio = []

for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_phones.append(product)
    elif product[4] == "Laptops":
        laptops.append(product)
    elif product[4] == "Audio":
        audio.append(product)

print("\n\nProducts by Category:")
print("-" * 60)

print("Mobile Phones:", mobile_phones)
print("Laptops:", laptops)
print("Audio:", audio)

# TODO 10: Calculate inventory statistics
total_products = len(inventory)

total_value = sum(product[2] * product[3] for product in inventory)

product_names = [product[1] for product in inventory]

product_prices = [product[2] for product in inventory]

print("\n\nInventory Statistics:")
print("-" * 60)

print("Total Products:", total_products)
print("Total Inventory Value:", total_value)
print("Product Names:", product_names)
print("Product Prices:", product_prices)

# TODO 11: Expensive products
expensive_products = [product for product in inventory if product[2] > 500]

print("\n\nExpensive Products (> $500):")
print("-" * 60)

print(expensive_products)

# TODO 12: Low stock alert
low_stock = [product for product in inventory if product[3] < 5]

print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)

print(low_stock)

# TODO 13: Price list comprehensions
original_prices = [product[2] for product in inventory]

discounted_prices = [price * 0.9 for price in original_prices]

print("\n\nPrice Lists:")
print("-" * 60)

print("Original Prices:", original_prices)
print("Discounted Prices:", discounted_prices)

# TODO 14: Product name formatting
uppercase_names = [product[1].upper() for product in inventory]

product_codes = [product[0][:3] + product[1][:3] for product in inventory]

print("\n\nFormatted Product Names:")
print("-" * 60)

print("Uppercase Names:", uppercase_names)
print("Product Codes:", product_codes)

# TODO 15: Using Loops to Process Inventory
mobile_count = 0
laptop_value = 0
most_expensive = inventory[0]

for product in inventory:

    if product[4] == "Mobile Phones":
        mobile_count += 1

    if product[4] == "Laptops":
        laptop_value += product[2] * product[3]

    if product[2] > most_expensive[2]:
        most_expensive = product

print("\n\nLoop-Based Analysis:")
print("-" * 60)

print("Mobile Phone Count:", mobile_count)
print("Total Laptop Value:", laptop_value)
print("Most Expensive Product:", most_expensive)

# TODO 16: Using Conditionals with Lists
restock_list = []
high_value_items = []

price_ranges = {
    "under_100": 0,
    "100_to_500": 0,
    "over_500": 0
}

for product in inventory:

    price = product[2]
    quantity = product[3]

    if quantity < 5:
        restock_list.append(product)

    if price > 500 and quantity > 10:
        high_value_items.append(product)

    if price < 100:
        price_ranges["under_100"] += 1
    elif price <= 500:
        price_ranges["100_to_500"] += 1
    else:
        price_ranges["over_500"] += 1

print("\n\nConditional Analysis:")
print("-" * 60)

print("Restock List:", restock_list)
print("High Value Items:", high_value_items)
print("Price Ranges:", price_ranges)

# TODO 17: Define and Use Functions

def calculate_product_value(product):
    return product[2] * product[3]

def find_products_by_category(inventory, category):
    return [product for product in inventory if product[4] == category]

def apply_discount(inventory, discount_percent):

    new_inventory = []

    for product in inventory:

        new_price = product[2] * (1 - discount_percent / 100)

        new_product = (
            product[0],
            product[1],
            new_price,
            product[3],
            product[4]
        )

        new_inventory.append(new_product)

    return new_inventory


total_inventory_value = sum(calculate_product_value(p) for p in inventory)

audio_products = find_products_by_category(inventory, "Audio")

discounted_inventory = apply_discount(inventory, 15)

print("\n\nFunction-Based Operations:")
print("-" * 60)

print("Total Inventory Value:", total_inventory_value)
print("Audio Products:", audio_products)
print("Inventory with 15% Discount:", discounted_inventory)

# TODO 18: Comprehensive inventory report

def generate_inventory_report(inventory):

    total_products = len(inventory)

    total_value = sum(product[2] * product[3] for product in inventory)

    categories = list(set(product[4] for product in inventory))

    low_stock = [product for product in inventory if product[3] < 5]

    average_price = sum(product[2] for product in inventory) / len(inventory)

    report = {
        "total_products": total_products,
        "total_value": total_value,
        "categories": categories,
        "low_stock": low_stock,
        "average_price": average_price
    }

    return report


report = generate_inventory_report(inventory)

print("\n\nComprehensive Inventory Report:")
print("-" * 60)

print(report)
