# store the list of users here
import pandas as pd
users = pd.DataFrame({
    "Name": ['Avi', 'Ammad', 'Moiz'],
    "Date of Birth": ['31-12-2000', '01-01-2001', '02-02-2002'],
    "ID Type": ["A","B","C"],
    "ID Number": [1, 2, 3],
    "Email": ["avi10malhotra@gmail.com", "todo", "todo"], #used as the primary key
    "Phone": [1, 2, 3],
    "Address": ['3495 University St. Presbyterian College', " todo", "todo"],
    "Zip Code": ["H3A 2A8", "todo", "todo"],
    "Orders": [],
})

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