print('hi\nmyname is : abdullah')
print("in this code we will do ")
#Dictionaries
print("Dictionaries")
print("\n\n")
#you can name any dictionary

dic_games = {"pc": ["rainbow", "pubg"], "ps4": ["last of us", "uncharted"]}
print(dic_games)
print(dic_games["pc"][1])
print("\n\n")
profile1 = {
    "ahmad": {
        "sport": {
            "team": "realmadrid",
            "player": "cr7"
        },
        "games": dic_games
    }
}

print(profile1)
print("\n\n")
#change the games now

dic_games1 = {"pc": ["the witcher 3", "GTA V"], "ps4": ["FIFA17", "overwatch"]}

profile2 = {
    "abdullah": {
        "sport": {
            "team": "barlcona",
            "player": "messi"
        },
        "games": dic_games1
    }
}

print(profile2)
print("\n\n")

profiles = {"num1": profile1, "num2": profile2}
print(profiles)