# Lists
print("Hello there! Welcome to the world of pokémon! My name is Oak! People call me the pokémon Prof! This world is inhabited by creatures called pokémon! ")
print("Nice to meet you, _____!")
yourname = input("What's your name? ")
print(f"Nice to meet you, {yourname}! ")
myPokemon = ["Charmander", "Squirtle", "Bulbasaur"]
print(f"I have here {len(myPokemon)} companions who are willing to assist you throughout your journey to becoming a Pokemon Master!")
print(myPokemon)
yourpokemon = input("Please choose one: ").lower() #.lower() makes your input in lowercase.
if yourpokemon == "charmander":
    print("You have chosen Charmander as your pokemon! The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.")
elif yourpokemon == "squirtle":
    print("You have chosen Squirtle as your pokemon! After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.")
elif yourpokemon == "bulbasaur": 
    print("You have chosen Bulbasaur as your pokeon! For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.")
else: 
    print("You're supposed to pick at least one of them, silly! ")
print("======================================================================================================================")
bugpokemon = ["Caterpie", "Volcarona", "Scyther"]
rockpokemon = ["Onix", "Geodude", "Aron"]
flyingpokemon = ["Zubat", "Dragonite", "Hawlucha"]
wildpokemon = [bugpokemon, rockpokemon, flyingpokemon]
print(f"You're exploring a cave and a wild {wildpokemon[1][1]} appeared!") #Geodude should be here
# HANGGANG DITO MUNA, BUKAS NA ULIT