# Q1: How many items did you purchase?
# Q2: How many items are free?
# Q3: What is the total amount you had to pay?
# Q4: What is the discount amount?
# Q5: What is the final amount you paid after the discount?
# Also: Include exception handling as per instructions.

def process_purchase_file():
    try:
        file_name = input("Enter the file name: ").strip()
        with open(file_name, "r") as file:
            lines = [line.strip() for line in file if line.strip() != ""]

        items = []
        discount = 0
        free_items = 0
        amount_to_pay = 0

        for line in lines:
            if line.lower().startswith("discount"):
                # Extract discount value
                try:
                    discount = int(line.split()[1])
                except (IndexError, ValueError):
                    print("Invalid discount format.")
                    return
            else:
                try:
                    name, price = line.split()
                    if price.lower() == "free":
                        free_items += 1
                    else:
                        price = int(price)
                        amount_to_pay += price
                        items.append((name, price))
                except ValueError:
                    print(f"Skipping invalid line: {line}")
                    continue

        total_items = len(items)
        final_amount = amount_to_pay - discount

        # Output
        print(f"No of items purchased: {total_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {amount_to_pay}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("The file you entered does not exist.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))


# Run the function
process_purchase_file()
