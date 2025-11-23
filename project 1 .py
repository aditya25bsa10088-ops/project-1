def generate_simple_bill():
    items = []
    total_amount = 0.0

    while True:
        item_name = input("Enter item name (or 'q' to finish): ")
        
        if item_name.lower() == 'q':
            break
        
        try:
            item_price = float(input(f"Enter price for {item_name}: $"))
            
            items.append((item_name, item_price))
            total_amount += item_price
            print("-" * 30)
            
        except ValueError:
            print("❌ Invalid price. Please enter a number.")
            continue

    print("\n" + "=" * 40)
    print("           ✨ Official Store Receipt ✨")
    print("=" * 40)
    
    print(f"{'Item':<25}{'Price':>15}")
    print("-" * 40)

    for name, price in items:
        print(f"{name:<25}${price:>.2f}")

    print("-" * 40)
    
    print(f"{'TOTAL AMOUNT DUE:':<25}${total_amount:>.2f}")
    
    print("=" * 40)
    print("      Thank you for shopping with us! 😊")

generate_simple_bill()