import user_registration
import recommendations
import availibility
import find_nearest_store

def main():
    print(
    """
        Hello, I JC - The Pharma Bot for Jean Coutu. I am here to help you with your needs.\n
        Please select one of the following options so that I can assist you better:\n
        \t1. This is my first time here, can you please register me as a user?\n
        \t2. I am looking for a specific medicine\n
        \t3. I am feeling unwell and would like to know what medicine I should take\n
        \t4. I would like to order some medicine and/or get a prescription refill\n
        \t5. I would like to know the closest JC Pharma store to me.\n
        
        Note: Please press 'Ctrl/Cmd + C' to exit the program at any time :)
    """)

    while True:
        response = input()
        match response:
            case "1":
                user_registration.register_user()
            case "2":
                availibility.check_availibility()
            case "3":
                recommendations.recommend_medicine()
            case "4":
                availibility.place_order()
            case "5":
                find_nearest_store.find_nearest_store()
            case _:
                print("Sorry, I did not understand your response. Please try again.")


if __name__ == '__main__':
    main()