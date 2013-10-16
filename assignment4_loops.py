#Mikah Woodward
#Assignment 4: Children's Song, the Sequel
#Prints a children's song


#calls verse functions
def main():
    # title
    title()
    
    # fly verse
    verse1()

    # spider verse
    verse2()

    # bird, cat, dog, monkey verses
    verses3_6()

    # horse verse
    lastverse()

#prints title
def title():
    print("There was an Old Lady")
    print()
    
#prints first line of each verse
def versebeginning(animal):
    print("There was an old lady who swallowed a", animal + punctuationchecker(animal))
    
def swallowed (first, second):
    
    print("She swallowed the", first, "to catch the", second + punctuationchecker(second))

#prints end of each verse, separated from the later verses since the ending of first verse is shorter
def flyend():
    print("I don't know why she swallowed the fly.")
    print("Perhaps she'll die.")
    print()

#prints end of 2nd verse and beyond
def verseend():
    print("That wriggled and jiggled and tickled inside her.")
    print("She swallowed the spider to catch the fly.")
    flyend()
    
#checks to see if last line is spider. If it is, replaces period with comma
def punctuationchecker(animal):
    if animal == 'spider':
        punctuation = ","
    else:
        punctuation = "."
    return punctuation
    
#verse functions

#verse 1
#calls versebeginning, then uses the shorter fly end    
def verse1():
    versebeginning('fly')
    flyend()

#verse 2
#calls verse beginning, then uses the longer verse ending, which will be used for everything besides the horse ending
def verse2():
    versebeginning('spider')
    verseend()
    


    
#verses 3 - 6
#these verses are almost exactly alike, so I figured I'd just throw them into a loop, with items being pulled from a list as necessary
#outer loop loops 4 times, once for each verse
#inner loop is the repeated 'swallowed' lines. It has one 'swallowed' line on the first verse ran, two on the second, etc.
animals = ['spider', 'bird', 'cat', 'dog', 'monkey']
sayings = ["How absurd to swallow a bird." , "Imagine that to swallow a cat." , "My what a hog, to swallow a dog.", "How funky, to swallow a monkey."]

def verses3_6():
    #loops 4 times, one for each verse
    for versecounter in range (4):
        versebeginning(animals[versecounter+1])
        print(sayings[versecounter])
        
        #runs through the swallowed loop one time on the first verse printed, twice on the second, etc
        #has to decrement instead of increment since the bigger animals are printed first
        #not only does versecounter determine how many swallowed loops are run, it also determines which animal the loop starts with
        for swallowedcounter in range (versecounter, -1, -1):
            swallowed(animals[swallowedcounter+1], animals[swallowedcounter])
        verseend()
    


#horse verse
def lastverse():
    print("There was an old lady who swallowed a horse.")
    print("She's dead, of course.")
    
    
    

# call main
main()
