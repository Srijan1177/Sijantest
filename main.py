# Main program for inventory system

from datetime import datetime
import read
import write
import operations

# Product storage file
PRODUCT_FILE = "products.txt"

def initialize_data():
    # Create sample data if file doesn't exist
    try:
        file = open(PRODUCT_FILE, "r")
        file.close()
    except:
        # Sample products
        sample_products = [
            "Vitamin C Serum, Garnier, 200, 1000, France",
            "Skin Cleanser, Cetaphil, 100, 280, Switzerland",
            "Sunscreen, Aqualogica, 200, 700, India",
            "Face Mask, Innisfree, 150, 450, South Korea",
            "Moisturizer, Neutrogena, 80, 550, USA"
        ]
        
        file = open(PRODUCT_FILE, "w")
        for product in sample_products:
            file.write(product + "\n")
        file.close()
        
        print("Sample product file created:", PRODUCT_FILE)

def display_welcome():
    # Show welcome message
    print("\n")
    print("\n")
    print("\t \t \t \tWeCare Skin\n")
    print("\t \tDurbar Marg, Kathmandu | Phone No: 9876543210\n")
    
    print("-" * 80)
    print("\t \t \tWelcome to the system!")
    print("-" * 80)
    print("\n")

def display_menu():
    # Show menu options
    print("-" * 80)
    print("Choose from the following to perform system operations.")
    print("-" * 80)
    
    print("Press 1 to sell products to customers.")
    print("Press 2 to buy products.")
    print("Press 3 to view current inventory.")
    print("Press 4 to exit from the system.")
    print("-" * 80)
    print("\n")

def main():
    # Initialize system
    initialize_data()
    display_welcome()
    products = read.read_products(PRODUCT_FILE)
    
    # Main program loop
    main_loop = True
    while main_loop == True:
        try:
            display_menu()
            options = int(input("Enter the option to continue: "))
            print("\n")
            
            if options == 1:
                # Sell products
                operations.sell_products(products, PRODUCT_FILE)
                
            elif options == 2:
                # Restock products
                operations.buy_products(products, PRODUCT_FILE)
                
            elif options == 3:
                # View inventory
                print("\nCurrent Inventory:")
                read.display_products(products)
                print("\nPress Enter to continue...")
                input()
                
            elif options == 4:
                # Exit
                main_loop = False
                print("Thank you for using the system!")
                print("\n")
                
            else:
                # Invalid option
                print("Your option,", options, ", does not seem to match our requirement. Please try again.")
                print("\n")
                
        except ValueError:
            print("Please enter a valid number!")
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
