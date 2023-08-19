import users_database

def place_order():
    print("Please enter your login details for verification before placing an order:\n")
    email = input("Please enter your email address:\n")
    password = input("Please enter your password:\n")

    user = users_database.check_login_details(email, password)

    if user is None:
        print("Sorry, your login details are incorrect. Please retry.")

    else:
        print("Please enter the details of your order, type 'Done' to finish placing your order:\n")
        while True:
            order = input("Please enter the full name of the product you want to order:\n").lower()
            if order == "done":
                break
            quantity = int(input(f"Please enter the order quantity for {order}:\n"))
            user['Orders'].append([order, quantity])

        print("""
        Thank you for your order! 
        A representative will contact you to verify the details of your PillPal prescription and you can then proceed with the payment.\n
        """)
