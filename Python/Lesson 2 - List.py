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
print(f"You're exploring a cave and a wild {wildpokemon[1][1]} appeared!") # Geodude should be here
# Converting list to tuples.  
action = ["FIGHT","BAG","POKeMON","RUN"]
actiontuples = tuple(action)
print(actiontuples)
skill = input(f"What will {yourpokemon} do? ").lower()
if skill == "fight":
    pokemonmove = ["Tackle","Growl"]
    print(pokemonmove)
    yourmove = input(f"What will {yourpokemon} do? ").lower()
    if yourmove == "tackle":
        print(f"{yourpokemon} deals 200 damage to {wildpokemon[1][1]}!")
        print(f"It was super effective! {wildpokemon[1][1]} fainted, you gained 10 exp!")
    elif yourmove == "growl":
        print(f"{yourpokemon} used growl!")
        print(f"{wildpokemon[1][1]} defense fell!")
        print(f"{wildpokemon[1][1]} ran away!")
if skill == "bag":
    print("Your bag is empty!")
elif skill == "pokemon":
    print("You have no other pokemon!")
elif skill == "run":
    print("Ran away safely.")
else:
    print("Please choose one of the four options!")