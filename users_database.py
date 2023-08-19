# store the list of users here
import pandas as pd
users = pd.DataFrame({
    "Name": ['Avi Malhotra', 'Ammad Shaikh', 'Syed Ammad Sohail'], # sample users
    "Date of Birth": ['31-12-2000', '02-02-1998', '10-09-2001'],
    "ID Type": ["A","B","C"],
    "ID Number": [11111, 22222, 33333],
    "Email": ["avi10malhotra@gmail.com", "todo", "todo"], # used as the primary key
    "Phone": [1234567890, 2244668800, 3216549870],
    "Address": ['3112 University Street', "todo", "todo"],
    "Zip Code": ["H3A 2B3", "H3B 1J5", "H3C 0J1"],
    "Orders": [{}, {}, {}],
})

# sample prescriptions
prescriptions = {
    "12345": {"patient_name": "Avi Malhotra", "birthdate": "31-12-2000", "medication": "Aspirin", "dosage": "100mg", "refills": 2},
    "67890": {"patient_name": "Ammad Shaikh", "birthdate": "02-02-1998", "medication": "Lisinopril", "dosage": "10mg", "refills": 1},
}

def addUser(user_info):
    global users
    users = users.append(user_info, ignore_index=True)

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