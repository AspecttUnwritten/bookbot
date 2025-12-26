import sys

from stats import get_num_words, letter_counter, list_creator, sort_on


def get_book_text(filename):
    with open(f"./{filename}") as bookf:
        book_content = bookf.read()
        return book_content


# print(get_book_text("/books/frankenstein.txt"))
# target1 = get_book_text("/books/frankenstein.txt")


# print(splitncount(target1))


def main(target):
    num_words = get_num_words(target)
    counter = letter_counter(target)
    list2sort = list_creator(counter)
    list2sort.sort(reverse=True, key=sort_on)
    # return f"Found {num_words} total words", list2sort
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for a in list2sort:
        print(f"{a['char']}: {a['num']}")
    print("============= END ===============")


# print(sys.argv)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file = get_book_text(sys.argv[1])
main(file)


# print(main(target1))
"""print(main(target1))

target2 = letter_counter(target1)

target3 = list_creator(target2)
print(target3)


target3.sort(reverse=True, key=sort_on)
print(target3)"""
