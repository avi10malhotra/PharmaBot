import pandas as pd

# read the data
df = pd.read_csv('medicine_dataset.csv', encoding='utf-8')

import nltk
import random

# set a random seed
random.seed(1)

def placeOrder(medicine):
    pass

def checkAvailibility(medicine):
    rand = random.randint(0, 1)
    if rand:
        print(f"{medicine} is available at atleast one of our stores. Would you like to place an order for home delivery?\n")
        response = input()
        if response == 'yes':
            print("Great! You are now being redirected to enter your delivery information and make the payment.\n")
        else:
            print("No worries, would you like us to tell you the list of stores where the medicine is available?\n")
            response = input()
            if response == 'yes':
                print("Here is the list of stores where the medicine is available:\n"
                      + "\t1. Downtown Pharmacy\n"
                      + "\t2. Saint Catherine Street\n"
                      + "\t3. Saint Laurent Boulevard\n")

            else:
                print("No worries, I hope that I answered all your questions! Please let me know if you have any other questions\n")
    else:
        alternatives = df[df['name'] == medicine][["substitute0", "substitute1", "substitute2", "substitute3", "substitute4"]]
        alternatives = alternatives.values[0].tolist()

        print(f"Sorry, unfortunately {medicine} is out of stock"
              + "However we do have the following alternatives available that are popularly used:\n")
        for alt in alternatives:
            if alt != 'nan':
                print('\t' + alt)

        print("We recommend cross-checking with a pharmacist to verify if the medicines can be interchanged\n")
    return

medicine = input("Please enter the medicine you are searching for: \n")

# search if the medicine is available in the dataset
matches = []
for med in df['name'].values:
    if med == medicine:
        checkAvailibility(med)
    elif med.startswith(medicine):
        matches.append(med)

if len(matches) == 0:
    print("Sorry, the medicine you are searching for is not available in our database.")
else:
    print("We found the following matches for your search: ")
    for match in matches:
        print(match)

    print("Please select the medicine you are searching for from the list above: ")
    medicine = input()
    checkAvailibility(medicine)



