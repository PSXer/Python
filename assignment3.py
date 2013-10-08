

def main():
    title()
    verse('chicken', 'cluck')
    verse('cow', 'moo')
    verse('duck', 'quack')
    extraverse()
    versequestion = input("Do you want another verse? yes/no ")
    if versequestion != "no":
        extraverse()

#prints each verse. 
def verse(animal, sound):
    #checks to see if animal and sound should be preceded by 'a' or 'an'
    bookend()
    print("And on that farm he had", articlechecker(animal), animal + ",", "E-I-E-I-O.")
    print("With", articlechecker(sound), sound + "-" + sound, "here, and", articlechecker(sound), sound + "-" + sound, "there.")
    print("Here", articlechecker(sound), sound, "there", articlechecker(sound), sound, "everywhere", articlechecker(sound), sound + "-" + sound + ".")
    bookend()
    print()

        

#prints title
def title():
    print("Old McDonald")
    print()

#beginning and end of each verse
def bookend():
    print("Old McDonald had a farm, E-I-E-I-O.")


#asks animal/sound names for user generated verses
def extraverse():
    animal = input ("enter an animal ")
    sound = input ("enter a sound ")
    verse(animal, sound)

#checks if a or an should be used in articles
def articlechecker(word):
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'u' or word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U': 
        article = "an"
    else:
        article= "a"
    return article        


#run main
main()
