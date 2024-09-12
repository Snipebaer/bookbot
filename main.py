def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)   
    print(text)

    num_words = word_count(text)
    print(f"\n{num_words} words in the text")

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def word_count(string):
    return len(string.split())

def get_number_of_each_char(text):
    char_in_text = {}
    
    for c in text:
        if c in char_in_text:
            char_in_text[c] += 1
        else:
            char_in_text[c] = 1
            
    return char_in_text

if __name__ == "__main__":
    #main()
    print(get_number_of_each_char("test"))    