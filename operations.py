# Functions for selling and restocking products

import read
import write

def buy_products(products, products_file):
    # Restock products function
    try:
        return restock_products(products, products_file)
    except Exception as e:
        print("Error in buy_products function:", str(e))
        return False

def restock_products(products, products_file):
    # Handle product restocking
    try:
        print("\nCurrent Inventory:")
        read.display_products(products)
        
        supplier_name = input("\nPlease enter the name of the Supplier: ")
        
        purchased_items = []
        total_cost = 0
        restock_loop = True
        
        while restock_loop == True:
            try:
                print("\nCurrent Inventory:")
                read.display_products(products)
                
                product_id = int(input("\nPlease provide the ID of the product you want to restock: "))
                
                if product_id <= 0 or product_id not in products:
                    print("Please provide a valid product ID!")
                    continue
                
                quantity = int(input("Please enter the quantity to add for " + products[product_id]['name'] + ": "))
                
                if quantity <= 0:
                    print("Please provide a valid quantity (greater than 0)!")
                    continue
                
                current_price = products[product_id]['price']
                
                item_total = quantity * current_price
                
                purchase_item = {
                    "id": product_id,
                    "name": products[product_id]["name"],
                    "brand": products[product_id]["brand"],
                    "quantity": quantity,
                    "price": current_price,
                    "total": item_total
                }
                
                purchased_items = purchased_items + [purchase_item]
                
                products[product_id]["quantity"] = products[product_id]["quantity"] + quantity
                
                total_cost = total_cost + item_total
                
                continue_restocking = input("\nDo you want to restock more items? (yes/no): ")
                if continue_restocking.lower() != "yes" and continue_restocking.lower() != "y":
                    restock_loop = False
                    
            except ValueError:
                print("Please enter a valid number!")
            except Exception as e:
                print("Error while adding product to restock:", str(e))
        
        if len(purchased_items) > 0:
            invoice_file = write.generate_purchase_invoice(supplier_name, purchased_items, total_cost)
            
            write.save_products(products, products_file)
            
            if invoice_file != None:
                print("\nHere is the purchase invoice:")
                read.read_invoice(invoice_file)
                
            print("\nThank you for restocking the products! Our inventory is now updated.")
        else:
            print("No items were restocked.")
            
        return True
        
    except Exception as e:
        print("Error in restock_products function:", str(e))
        return False

def sell_products(products, products_file):
    # Process sales to customers
    try:
        print("\nAvailable Products:")
        read.display_products(products)
        
        print("\nFor Bill Generation you will have to enter your details first:")
        print("-" * 70)
        name = input("Please enter the name of the Customer: ")
        phone_number = input("Please enter the phone number of the Customer: ")
        print("\n")
        
        cart_items = []
        total_bill = 0
        total_free_items = 0
        sell_loop = True
        
        while sell_loop == True:
            try:
                print("\nAvailable Products:")
                read.display_products(products)
                
                product_id = int(input("Please Provide the ID of the product you want to sell: "))
                
                if product_id <= 0 or product_id not in products:
                    print("Please provide a valid product ID!")
                    continue
                
                print("\n")
                product_quantity = int(input("Please Provide the number of quantity of the product you want to sell: "))
                print("\n")
                
                if product_quantity <= 0:
                    print("Please provide a valid quantity (greater than 0)!")
                    continue
                
                free_items = product_quantity // 3
                total_quantity_to_deduct = product_quantity + free_items
                
                if total_quantity_to_deduct > products[product_id]["quantity"]:
                    print("Dear Admin, the quantity you are looking for is not available in our shop. Please try again.")
                    print("Available quantity:", products[product_id]["quantity"])
                    continue
                
                selling_price = products[product_id]["price"] * 2
                item_total = selling_price * product_quantity
                
                cart_item = {
                    "id": product_id,
                    "name": products[product_id]["name"],
                    "brand": products[product_id]["brand"],
                    "quantity": product_quantity + free_items,
                    "paid_quantity": product_quantity,
                    "free_quantity": free_items,
                    "price": selling_price,
                    "total": item_total
                }
                
                cart_items = cart_items + [cart_item]
                
                total_bill = total_bill + item_total
                total_free_items = total_free_items + free_items
                
                if free_items > 0:
                    print("Dear", name, ", we are having buy 3 get one free offer, hence you have received", free_items, "free items!")
                
                products[product_id]["quantity"] = products[product_id]["quantity"] - total_quantity_to_deduct
                
                continue_shopping = input("\nDo you want to purchase more items? (yes/no): ")
                if continue_shopping != "yes" and continue_shopping != "y":
                    sell_loop = False
                    
            except ValueError:
                print("Please enter a valid number!")
            except:
                print("Error while adding product to cart!")
        
        if len(cart_items) > 0:
            invoice_file = write.generate_sales_invoice(name, phone_number, cart_items, total_bill, total_free_items)
            
            write.save_products(products, products_file)
            
            if invoice_file != None:
                print("\nHere is the invoice:")
                read.read_invoice(invoice_file)
        else:
            print("No items were purchased.")
            
        return True
        
    except:
        print("Error in sell_products function!")
        return False
