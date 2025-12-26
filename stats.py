# this splits the word up i think
def get_num_words(target):
    result = len(target.split())
    return result


# this gets the number of letters in a word
def letter_counter(string):
    dict_count = {}
    for a in string:
        if not a == " ":
            b = a.lower()
            if b not in dict_count:
                dict_count[b] = 1
            else:
                dict_count[b] += 1
    return dict_count


def list_creator(list):
    output_dict = []
    for a in list:
        output_dict.append({"char": a, "num": list[a]})

    return output_dict


def sort_on(items):
    return items["num"]


"""
def sort_keynum(items):
    return items[num]"""
