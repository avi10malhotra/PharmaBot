import user_functions
import recommendations
import availibility
import find_nearest_store
import order
import prescription_refill
import fetch_google_forms

def main():
    print(
    """
        Hello, I PillPal - The Pharma Bot for Jean Coutu. I am here to help you with your needs.\n
        Please select one of the following options so that I can assist you better:
        \t1. This is my first time here, can you please register me as a user? 
        \t2. I am looking for a specific medicine
        \t3. I am feeling unwell and would like to know what medicine I should take
        \t4. I would like to order some medicine and/or get a prescription refill
        \t5. I would like to know the closest JC Pharma store to me.
        \t6. I would like to refill my prescription
        
        Note: Please type 'quit' to exit the program at any time 😁
    """)

    while True:
        response = input()
        if response.__contains__("quit"):
            print("Thank you for using PillPal! Have a great day!")
            exit()
        match response:
            case "1":
                print("Welcome to Jean Coutu! 🥳Please register here: ")
                is_done = input("Have you filled the Google form? (Y/N) \n")
                if is_done == "Y":
                    new_user = fetch_google_forms.fetch_new_user()
                    if new_user is not None:
                        user_functions.addUser(new_user)
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