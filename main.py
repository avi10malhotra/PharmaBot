import user_registration
import recommendations
import availibility
import find_nearest_store
import order
import prescription_refill

def main():
    print(
    """
        Hello, I PillPal - The Pharma Bot for Jean Coutu. I am here to help you with your needs.\n
        Please select one of the following options so that I can assist you better:\n
        \t1. This is my first time here, can you please register me as a user? \n
        \t2. I am looking for a specific medicine\n
        \t3. I am feeling unwell and would like to know what medicine I should take\n
        \t4. I would like to order some medicine and/or get a prescription refill\n
        \t5. I would like to know the closest JC Pharma store to me.\n
        \t6. I would like to refill my prescription\n
        
        Note: Please press 'Ctrl/Cmd + C' to exit the program at any time 😁
    """)

    while True:
        response = input()
        match response:
            case "1":
                print("Welcome to Jean Coutu! 🥳Please register here: ")
                user_registration.register_user()
            case "2":
                medicine = input("Please enter the medicine you are searching for 🔍: \n")
                availibility.is_available(medicine)
            case "3":
                symptoms = input("I am sorry to hear that! 😕 Please describe your symptoms or specify the kind of medicine you are looking for : ")
                recommendations.recommend_medicine(symptoms)
            case "4":
                order.place_order()
            case "5":
                find_nearest_store.find_nearest_store()
            case "6":
                prescription_refill.refill_request()
            case _:
                print("Sorry, I did not understand your response. Can you please choose one of the 6 options? 😅")


if __name__ == '__main__':
    main()