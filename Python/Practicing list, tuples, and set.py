# Practicing Tuples, Set, and Lists. 
# Basic Examples

# List = [] ordered and changeable. Duplicates OK


pokemon = ["Pikachu", "Charmander", "Greninja", "Meowth", "Jigglypuff", "Onyx", "Arceus"]
# print(dir(pokemon)) (This will tell you the commands / syntax you can use)
# print(help(pokemon)) 
# print(len(pokemon)) # counts the amount of element inside the list.
# print("Zapdos" in pokemon) # checks whether the element is inside the list or not

# pokemon[0] = "Articuno" # puts 
# pokemon.append("Evee") # puts evee in the last position
# pokemon.remove("Arceus") 
# pokemon.insert(0, "Squirtle")
# pokemon.sort() # arranges alphabetically
# pokemon.reverse() # arranges element in reverse
# pokemon.clear() # all elements are removed
# print(pokemon.index("Onyx")) if printed, output will be 5


# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Best use if we're doing constants

# immutable - we can't alter the value.
# pokemon.add("Arceus")
# pokemon.remove("Meowth")
# pokemon.pop() - Remove the firs one but doesn't really matter since its random 
# pokemon.clear() - Clears the set

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER
# pokemon.index("Arceus")
# pokemon.count("Onyx") ; output is 1;
for pokemons in pokemon:
    print(pokemons)