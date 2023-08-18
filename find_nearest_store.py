from pgeocode import GeoDistance
import users_database

import store_locations


# finds the closest JC Pharma store to the user's zip address using the pgeocode library
def find_closest_JC(user_zip, target_zips):
    geo_dist = GeoDistance('CA')

    closest_zip = None
    min_distance = float("inf")

    # calculate the distance between the user's zip code and each of the target zip codes
    for target_zip in target_zips:
        distance = geo_dist.query_postal_code(user_zip, target_zip)

        if distance < min_distance:
            min_distance = distance
            closest_zip = target_zip

    return closest_zip


# print(find_closest_JC('H3A 3A8', JC_locations.values()))

# use the user's default address
user_location = input("Do you want me to recommend the closest JC Pharma store to your home address? (yes/no)\n")
if user_location == 'yes':
    print("Please enter your login details for verification code:\n")
    email = input("Please enter your email address:\n")
    password = input("Please enter your password:\n")

    # verify user authentication
    user = users_database.check_login_details(email, password)

    if user is None:
        print("Sorry, your login details are incorrect. Please retry.")

    else:
        closest_JC = find_closest_JC(user["Zip"], JC_locations.values())
    print(f"The closest JC Pharma store to you is located at {closest_JC}\n")

# the user manually inserts a zip code
else:
    code = input("Please enter the zip code:\n")
    closest_JC = find_closest_JC(code, JC_locations.values())
    print(f"The closest Jean Coutu store to your location ({code}) is located at {closest_JC}\n")
