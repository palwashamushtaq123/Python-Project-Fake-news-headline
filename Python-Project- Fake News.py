import random
subject_list = [
    "Atif Aslam",
    "Asim Raza",
    "Shehzad Rao",
    "A Russian Cat",
    "A Group of Monkeies",
    "CM Mariam Nawaz",
    "A auto Driver from Pakistan",
]

actions_list = [
    "Lunches",
    "Cancels",
    "Dances with",
    "Eats",
    "Declares war on",
    "Orders",
    "Celebrates",
]

places_or_things_list = [
    "at port grand",
    "in Pkaistan local train",
    "a palate of Golghapa",
    "inside parliament",
    "at sabzi market",
    "during IPL match",
    "at Pakistan gate",
]
while True:
    subject = random.choice(subject_list)
    actions = random.choice(actions_list)
    places_or_things = random.choice(places_or_things_list)

    Headline = f" BREAKING NEWS: {subject} {actions} {places_or_things}"
    print("\n" + Headline)
    user_input = input("\nDo you want to another headline? (yes/no)").strip().lower()
    
    if user_input == "no":
        break
#print goodbye message      
print("\nThanks for using the Fake News Headline Generator.Have a fun day...")
