def main():

    path = "/Users/furentsu/programming/github.com/Furentsu/bookbot/books/frankenstein.txt"
    
    with open(path) as f:
        file_contents =f.read()
        print(count_words(file_contents))

# Function to count the number of words in the text
def count_words(text):
    words = text.split()
    return len(words)

main()