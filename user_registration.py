#This scenario is to ask users to register if they are not an exisiting user:

from users_database import users

def collect_user_information():
    name = input("Please enter your name: ")
    dob = input("Please enter your date of birth (e.g., YYYY-MM-DD): ")
    id_type = input("Please enter the type of your government issued ID (e.g., Passport, Driver's License, Permanent Residence Card, Health Insurance): ")
    id_number = input("Please enter your ID number: ")
    email = input("Please enter your email address: ")
    phone = input("Please enter your phone number: ")
    address = input("Please enter your address: ")
    zip = input("Please enter your zip code: ")

    user_info = {
        "Name": name,
        "Date of Birth": dob,
        "ID Type": id_type,
        "ID Number": id_number,
        "Email": email, #used as the primary key
        "Phone": phone,
        "Address": address,
        "Zip Code": zip,
        "Orders": [],
    }

    users.addUser(user_info)

    return user_info

user_data = collect_user_information()
print("\nCollected Information:")
for key, value in user_data.items():
    print(f"{key}: {value}")
