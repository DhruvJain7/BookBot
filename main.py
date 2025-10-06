import sys
from stats import count_words
from stats import count_character
from stats import list_dict
def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
        return file_contents

def main():
    if(len(sys.argv)!=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        answer = get_book_text(path)
        num_words = count_words(answer)
        char = count_character(answer)
        print("========== BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("---------- Word Count ------------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        l = list_dict(char)
        for i in l:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
            else:
                continue
        print("============ END ============")
main()


