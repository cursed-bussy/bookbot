def count_words(transcript):
    words = transcript.split()
    total_word_count = len(words)
    return total_word_count

def count_characters(transcript):
    transcript = transcript.lower()
    char_count = {}
    for char in transcript:
        if char.isalpha():  # Check if the character is a letter
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def print_report(word_count, char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")

def main():
    with open("frankenstein.txt") as f:
        file_contents = f.read()

    # Calculate word count
    word_count = count_words(file_contents)

    # Calculate character count
    char_counts = count_characters(file_contents)

    # Print the report
    print_report(word_count, char_counts)

if __name__ == "__main__":
    main()
