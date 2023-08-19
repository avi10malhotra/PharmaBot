from user_functions import prescriptions

def verify_patient(prescription_id):
    print("For security, please verify some details.")
    name = input("Enter your full name: ")
    birthdate = input("Enter your birthdate (MM-DD-YYYY): ")

    if (name == prescriptions[prescription_id]["patient_name"] and
        birthdate == prescriptions[prescription_id]["birthdate"]):
        return True
    else:
        print("Verification failed. Please ensure you're entering correct details.")
        return False

def refill_request():
    prescription_id = input("Please enter your prescription ID: ")

    if prescription_id in prescriptions:
        if not verify_patient(prescription_id):
            return

        medication = prescriptions[prescription_id]["medication"]
        dosage = prescriptions[prescription_id]["dosage"]
        refills = prescriptions[prescription_id]["refills"]

        if refills > 0:
            prescriptions[prescription_id]["refills"] -= 1
            print(f"Your refill request for {medication} {dosage} has been processed. "
                  f"You now have {prescriptions[prescription_id]['refills']} refills left.")

            # Ask about delivery options
            delivery = input("Would you like the medication delivered to your address? (yes/no): ").strip().lower()
            if delivery == "yes":
                print("Great! Your medication will be delivered to your address.")
            else:
                print("Alright! You can pick up your medication from our pharmacy.")

            # Ask for refill reminders
            reminder = input("Would you like a reminder for your next refill? (yes/no): ").strip().lower()
            if reminder == "yes":
                print("We'll remind you when it's time for your next refill.")
        else:
            print(f"You have no refills left for {medication} {dosage}. Please contact your doctor.")
    else:
        print("Invalid prescription ID. Please check and try again.")

