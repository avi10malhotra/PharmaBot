import user_functions

def place_order():
    print("Please enter your login details for verification before placing an order:\n")
    email = input("Please enter your email address:\n")
    identification = input("Please enter your registration id number:\n")

    user = user_functions.check_login_details(email, identification)

    if user is None:
        print("Sorry, your login details are incorrect. Please retry.")

    else:
        print("Please enter the details of your order, type 'Done' to finish placing your order:\n")
        total_order = {}
        while True:
            order = input("Please enter the full name of the product you want to order:\n").lower()
            if order == "done":
                break
            quantity = int(input(f"Please enter the order quantity for {order}:\n"))
            total_order[order] = quantity

        print("""
        Thank you for your order! 
        A representative will contact you to verify the details of your PillPal prescription and you can then proceed with the payment.\n
        """)

        with open("order_details.txt", "w") as file:
            file.write(f"Order for id {identification} with email {email}:\n")
            for order, quantity in total_order.items():
                file.write(f"{order} - {quantity}\n")
