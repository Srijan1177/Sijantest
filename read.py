# Functions for reading product data

def read_products(filename):
    # Read products from file and return as dictionary
    products = {}
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        
        product_id = 1
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
                
            if not line:
                continue
                
            data = line.split(', ')
            
            if len(data) >= 5:
                name = data[0]
                brand = data[1]
                try:
                    quantity = int(data[2])
                    price = float(data[3])
                    origin = data[4]
                    
                    products[product_id] = {
                        'name': name,
                        'brand': brand,
                        'quantity': quantity,
                        'price': price,
                        'origin': origin
                    }
                    product_id += 1
                except (ValueError, IndexError) as e:
                    print("Warning: Error processing line:", line, "Error:", e)
            else:
                print("Warning: Insufficient data in line:", line, "Expected at least 5 values.")
    except Exception as e:
        print("Error reading product file:", e)
    
    return products

def display_products(products):
    # Show products in formatted table
    if not products:
        print("No products available.")
        return
    
    print("-" * 100)
    print("{:<5} {:<20} {:<15} {:<8} {:<15} {:<15} {:<15}".format(
        "ID", "Product", "Brand", "Qty", "Cost Price", "Selling Price", "Country"))
    print("-" * 100)
    
    for product_id in products:
        product = products[product_id]
        
        selling_price = product['price'] * 2
        
        cost_price_str = format(product['price'], '.2f')
        selling_price_str = format(selling_price, '.2f')
        
        print("{:<5} {:<20} {:<15} {:<8} {:<15} {:<15} {:<15}".format(
            product_id,
            product['name'][:20],
            product['brand'][:15],
            product['quantity'],
            "Rs. " + cost_price_str,
            "Rs. " + selling_price_str,
            product['origin'][:15]))
    
    print("-" * 100)

def read_invoice(filename):
    # Display invoice content
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        
        print(content)
    except:
        print("Error reading invoice:", filename)
