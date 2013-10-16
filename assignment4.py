#Mikah Woodward
#Assignment 4: Children's Song, the Sequel
#Prints a children's song

def main():
    # title
    title()

    # fly verse
    verse1()

    # spider verse
    verse2()

    # bird verse
    verse3()

    # cat verse
    verse4()

    # dog verse
    verse5()

    # extra verse
    verse6()

    # horse verse
    lastverse()

#prints title
def title():
    print("There was an Old Lady")
    print()
    
#prints first line
def versebeginning(animal):
    print("There was an old lady who swallowed a", animal +'.')
    
def swallowed (first, second):
    if second == 'spider':
        punctuation = ","
    else:
        punctuation = "."
    print("She swallowed the", first, "to catch the", second + punctuation)

def spiderend():
    print("That wriggled and jiggled and tickled inside her.")
    print("She swallowed the spider to catch the fly")
    
#prints end of each verse
def verseend():
    print("I don't know why she swallowed the fly.")
    print("Perhaps she'll die.")
    print()

def verse1():
    versebeginning('fly')
    verseend()

def verse2():
    versebeginning('spider')
    spiderend()
    verseend()

def verse3():
    versebeginning('bird')
    print("How absurd to swallow a bird.")
    swallowed('bird', 'spider')
    spiderend()
    verseend()

def verse4():
    versebeginning('cat')
    print("Imagine that to swallow a cat.")
    swallowed('cat', 'bird')
    swallowed('bird', 'spider')
    spiderend()
    verseend()

def verse5():
    versebeginning('dog')
    print("My what a hog, to swallow a dog.")
    swallowed('dog', 'cat')
    swallowed('cat', 'bird')
    swallowed('bird', 'spider')
    spiderend()
    verseend()

def verse6():
    versebeginning('monkey')
    print("How funky, to swallow a monkey.")
    swallowed('monkey', 'dog')
    swallowed('dog', 'cat')
    swallowed('cat', 'bird')
    swallowed('bird', 'spider')
    spiderend()
    verseend()

def lastverse():
    print("There was an old lady who swallowed a horse.")
    print("She's dead, of course.")
    
    
    

# call main
main()
