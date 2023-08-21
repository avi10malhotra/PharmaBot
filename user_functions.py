# store the list of users here
import csv


def add_user(user_info):
    user_info = user_info[1:]
    # write the user_info list to the users.csv file
    with open("users.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(user_info)
    f.close()

    # print user info to the console
    print("User added successfully!")
    print("Name: " + user_info[0])
    print("Date of Birth: " + user_info[3])
    print("ID Type: " + user_info[1])
    print("ID Number: " + user_info[2])
    print("Email: " + user_info[4])
    print("Phone: " + user_info[5])
    print("Address: " + user_info[7])
    print("Zip Code: " + user_info[6])


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


