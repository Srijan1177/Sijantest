# Functions for writing data to files

import datetime

def save_products(products, filename):
    # Save products to file
    try:
        file = open(filename, "w")
        for product_id in products:
            product = products[product_id]
            line = product['name'] + ", " + product['brand'] + ", " + str(product['quantity']) + ", " + str(product['price']) + ", " + product['origin'] + "\n"
            file.write(line)
        file.close()
        return True
    except:
        print("Error saving products to file:", filename)
        return False

def generate_sales_invoice(customer_name, customer_phone, items_sold, total_amount, free_items):
    # Create sales invoice file
    try:
        current_time = datetime.datetime.now()
        invoice_name = "sales_invoice_" + current_time.strftime('%Y%m%d_%H%M%S') + ".txt"
        
        file = open(invoice_name, "w")
        
        # Header
        file.write("-" * 80 + "\n")
        file.write("\t \t \tWeCare Skin\n")
        file.write("\t \tDurbar Marg, Kathmandu | Phone No: 9876543210\n")
        file.write("-" * 80 + "\n\n")
        
        # Invoice details
        file.write("SALES INVOICE\n")
        file.write("Date: " + current_time.strftime('%Y-%m-%d %H:%M:%S') + "\n")
        file.write("Customer Name: " + customer_name + "\n")
        file.write("Customer Phone: " + customer_phone + "\n\n")
        
        # Items table header
        file.write("-" * 80 + "\n")
        file.write("{:<5} {:<20} {:<15} {:<8} {:<15} {:<15}\n".format(
            "ID", "Product", "Brand", "Qty", "Unit Price", "Total"))
        file.write("-" * 80 + "\n")
        
        # Process items
        for item in items_sold:
            price_str = format(item['price'], '.2f')
            total_str = format(item['total'], '.2f')
            
            paid_quantity = int(item['total'] / item['price'])
            free_quantity = item['quantity'] - paid_quantity
            
            # Paid items
            file.write("{:<5} {:<20} {:<15} {:<8} {:<15} {:<15}\n".format(
                item['id'],
                item['name'][:20],
                item['brand'][:15],
                paid_quantity,
                price_str,
                total_str))
            
            # Free items
            if free_quantity > 0:
                file.write("{:<5} {:<20} {:<15} {:<8} {:<15} {:<15}\n".format(
                    item['id'],
                    item['name'][:20] + " (FREE)",
                    item['brand'][:15],
                    free_quantity,
                    "0.00",
                    "0.00"))
        
        file.write("-" * 80 + "\n")
        
        # Summary
        file.write("\nSubtotal: Rs. " + format(total_amount, '.2f') + "\n")
        
        if free_items > 0:
            file.write("Free Items: " + str(free_items) + " (Buy 3 Get 1 Free Offer)\n")
            
        file.write("Grand Total: Rs. " + format(total_amount, '.2f') + "\n\n")
        
        file.write("Thank you for shopping with us!\n")
        file.write("=" * 80 + "\n")
        
        file.close()
        
        print("Sales invoice generated:", invoice_name)
        return invoice_name
    except Exception as e:
        print("Error generating sales invoice:", str(e))
        return None
    
def generate_purchase_invoice(supplier_name, items_purchased, total_amount):
    # Create purchase invoice file
    try:
        current_time = datetime.datetime.now()
        invoice_name = "purchase_invoice_" + current_time.strftime('%Y%m%d_%H%M%S') + ".txt"
        
        file = open(invoice_name, "w")
        
        # Header
        file.write("-" * 80 + "\n")
        file.write("\t \t \tWeCare Skin\n")
        file.write("\t \tDurbar Marg, Kathmandu | Phone No: 9876543210\n")
        file.write("-" * 80 + "\n\n")
        
        # Invoice details
        file.write("PURCHASE INVOICE\n")
        file.write("Date: " + current_time.strftime('%Y-%m-%d %H:%M:%S') + "\n")
        file.write("Supplier: " + supplier_name + "\n\n")
        
        # Items table header
        file.write("-" * 80 + "\n")
        file.write("{:<5} {:<20} {:<15} {:<8} {:<15} {:<15}\n".format(
            "ID", "Product", "Brand", "Qty", "Unit Price", "Total"))
        file.write("-" * 80 + "\n")
        
        # Items list
        for item in items_purchased:
            price_str = format(item['price'], '.2f')
            total_str = format(item['total'], '.2f')
            
            file.write("{:<5} {:<20} {:<15} {:<8} {:<15} {:<15}\n".format(
                item['id'],
                item['name'][:20],
                item['brand'][:15],
                item['quantity'],
                price_str,
                total_str))
        
        file.write("-" * 80 + "\n")
        
        # Summary
        file.write("\nTotal Amount: Rs. " + format(total_amount, '.2f') + "\n\n")
        file.write("Thank you for your business!\n")
        file.write("=" * 80 + "\n")
        
        file.close()
        
        print("Purchase invoice generated:", invoice_name)
        return invoice_name
    except:
        print("Error generating purchase invoice!")
        return None
