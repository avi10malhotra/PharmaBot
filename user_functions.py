# store the list of users here
import csv

# create an empty csv with these headers: Name	ID Number	ID Type	Date of Birth	Email	Phone	Zip Code	Address	Orders
# with open("users.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "ID Number", "ID Type", "Date of Birth", "Email", "Phone", "Zip Code", "Address", "Orders"])

# sample prescriptions
prescriptions = {
    "12345": {"patient_name": "Avi Malhotra", "birthdate": "31-12-2000", "medication": "Aspirin", "dosage": "100mg", "refills": 2},
    "67890": {"patient_name": "Ammad Shaikh", "birthdate": "02-02-1998", "medication": "Lisinopril", "dosage": "10mg", "refills": 1},
}



def addUser(user_info):
    user_info = user_info[1:]
    # write the user_info list to the users.csv file
    with open("users.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(user_info)
    f.close()

def check_login_details(email, password):
    for user in users:
        if user['Email'] == email and user['Password'] == password:
            return user
    return None

def add_order(email, order) -> bool:
    for user in users:
        if user['Email'] == email:
            user['Orders'].append(order)
            return True
    return False


