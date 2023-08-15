import pandas as pd

# read the data
df = pd.read_csv('medicine_dataset.csv', encoding='utf-8')


from rake_nltk import Rake

sentence = input("Please describe your symptoms or specify the kind of medicine you are looking for: ")

r = Rake()

# Extract keywords from the sentence
r.extract_keywords_from_text(sentence)

# Get the keywords
keywords = r.get_ranked_phrases()

if len(keywords) > 1:
    print("I cannot recommend you a medicine based on your symptoms. It is advised that you see a physician.")
    exit()

# lower every value in df['use0']
df['use0'] = df['use0'].str.lower()

# search if a corresponding medicine is available in the dataset
matches_id = []
# ennumerate over every row in the dataframe
for index, row in df.iterrows():
    if keywords[0].__contains__(row['use0']):
        matches_id.append(index)


if len(matches_id) == 0:
    print("I would advise you to speak with one of our pharmacist to find a medicine that is best suited for our needs.")
else:
    print("We have the following medicines available : ")
    matches_id = matches_id[:3]
    for id in matches_id:
        medicine = df.iloc[id]
        print(f"""
        Name: {medicine['name']}\n
        Usage: {medicine['use0']}\n
        Potential Side Effect: {medicine['sideEffect0']}\n
        Chemical Class: {medicine['Chemical Class']}\n
        Habit Forming: {medicine['Habit Forming']}\n
        Therapeutic Class: {medicine['Therapeutic Class']}\n\n
        """)





