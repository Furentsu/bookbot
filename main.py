import json

def main():

    path = "/Users/furentsu/programming/github.com/Furentsu/bookbot/books/frankenstein.txt"
    
    with open(path) as f:
        file_contents =f.read()
        print("Total characters in the book: \n", json.dumps(count_characters_occurrencies(file_contents), indent=4, sort_keys=True))
        print("\nTotal words: ", count_words(file_contents))

# Function to count the number of words in the text
def count_words(text):
    words = text.split()
    return len(words)

# Function to count the number of characters occurrencies in the text
def count_characters_occurrencies(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

main()