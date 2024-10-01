def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)

    chars_dict = get_character_count(book_text)
    
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()
    


def get_num_words(text):
    return len(text.split())



def sort_on(d):
    return d["num"]




def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



def get_character_count(text):
    character_count = {}

    for character in text:
        lowered = character.lower()
        if (lowered in character_count):
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1

    return character_count



main()