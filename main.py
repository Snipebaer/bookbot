def main():
    file_path = "books/frankenstein.txt"
    print_report(file_path)    

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def word_count(string):
    return len(string.split())

def get_number_of_each_char(text):
    char_in_text = {}    
    
    for c in text.lower():

        if c == ' ' or c == '\n':
            continue
        
        if c in char_in_text:
            char_in_text[c] += 1
        else:
            char_in_text[c] = 1

    return char_in_text 

def sort_on(item):
    return item[1]

def print_report(file_path):
    print(f"--- Begin report of {file_path} ---")

    text = get_book_text(file_path)

    # get number of words from the text
    num_words = word_count(text)
    print(f"{num_words} words found in the document\n\n")

    # print number of each char (not case-sensitive)
    num_chars = get_number_of_each_char(text)
    sorted_chars = sorted(num_chars.items(), key=sort_on, reverse=True)
    for char, count in sorted_chars:
        print(f"'{char}': {count}")

    print("\n--- End of report ---")  

if __name__ == "__main__":
    main()
      