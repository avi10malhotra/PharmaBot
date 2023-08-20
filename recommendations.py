import pandas as pd
from rake_nltk import Rake

# read the data and create the Rake object
df = pd.read_csv('medicine_dataset.csv', encoding='utf-8')
r = Rake(stopwords=None, punctuations={".", ",", ";", "!"}, language='english')


def find_medicine():
    medicine = input("Please enter the medicine you are searching for: \n")

    # search if the medicine is available in the dataset
    matches = []
    for med in df['name'].values:
        if med == medicine:
            matches.append(med)
        elif med.startswith(medicine):
            matches.append(med)

    if len(matches) == 0:
        print("Sorry, the medicine you are searching for is not available in our database.")
    else:
        print("We found the following matches for your search: ")
        for match in matches:
            print(match)

    return matches


# searches the medicine database to find the medicine that matches the user's description
def recommend_medicine(sentence):
    # Extract keywords from the sentence using RAKE heuristics
    r.extract_keywords_from_text(sentence)

    # Get the keywords
    keywords = r.get_ranked_phrases()

    while True:
        # user description is valid
        if len(keywords) == 1:
            break

        # user description is too complex
        else:
            print("Sorry, your symptoms are too complex for me to understand.\n"
                  + "I would suggest that you speak to a physician for a better diagnosis.\n"
                  + "Alternatively, you can try describing your symptoms using keywords.\n")

            sentence = input()

            # check if the user wants to quit
            if sentence.__contains__("quit" or "exit"):
                print("I apologize once again for not being able to help you. Have a great day!")
                exit()

            r.extract_keywords_from_text(sentence)
            keywords = r.get_ranked_phrases()

    if len(keywords) > 1:
        print("I cannot recommend you a medicine based on your symptoms. It is advised that you see a physician.")
        exit()

    # lower every value in df['use0'] which stores the medicine usage
    df['use0'] = df['use0'].str.lower()

    # search if a corresponding medicine is available in the dataset
    matches_id = []

    # enumerate over every row in the dataframe and check if the medicine usage contains the keyword
    for index, row in df.iterrows():
        if row['use0'].__contains__(keywords[0]):
            matches_id.append(index)

    # no medicine found
    if len(matches_id) == 0:
        print(
            "Unfortunately, I couldn't find a medicine for you. I would advise you to speak with one of our pharmacist to find a medicine that is best suited for our needs.")

    # medicine found; user is shown the top 3 results with relevant medicine information
    else:
        print("We have the following medicines available : ")
        matches_id = matches_id[:3]
        for id in matches_id:
            medicine = df.iloc[id]
            print(f"\tName: {medicine['name']}")
            print(f"\tUsage: {medicine['use0']}")
            print(f"\tPotential Side Effect: {medicine['sideEffect0']}")
            print(f"\tChemical Class: {medicine['Chemical Class']}")
            print(f"\tHabit Forming: {medicine['Habit Forming']}")
            print(f"\tTherapeutic Class: {medicine['Therapeutic Class']}\n")

