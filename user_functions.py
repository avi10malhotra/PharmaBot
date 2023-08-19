# store the list of users here
import csv

def addUser(user_info):
    user_info = user_info[1:]
    # write the user_info list to the users.csv file
    with open("users.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(user_info)
    f.close()

def check_login_details(email, id):
    # open the users.csv file and search for the user with the given email and password
    with open("users.csv", "r") as f:
        reader = csv.reader(f)
        users = list(reader)
    f.close()

    for user in users[1:]:
        if user[4] == email and user[2] == id:
            return user
    return None


