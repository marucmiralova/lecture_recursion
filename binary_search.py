import os
import json

cwd_path = os.getcwd()
file_path = "files"


def read_data(file_name, key="ordered_numbers"):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, str), sequential data
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), mode="r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]


def binary_search(seq, number):
    """
    Function performs binary search on !!ordered!! sequence and stores position of match if found.
    :param seq: (list): list of numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    """
    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle
    return None

def binary_search_rec(seq, number, idx_vlevo, idx_vpravo):
    # if idx_vlevo >= idx_vpravo:
    #     return None
    # else:
    middle = (idx_vpravo + idx_vlevo) // 2
    if number == seq[middle]:
        return middle
    elif idx_vlevo == idx_vpravo:
        return None
    elif number < seq[middle]:
        return binary_search_rec(seq, number, idx_vlevo, middle-1)
    elif number > seq[middle]:
        return binary_search_rec(seq, number, middle+1, idx_vpravo)



def main(file_name, number):
    sequence = read_data(file_name=file_name, key="ordered_numbers")

    # iterative binary search
    print(binary_search(sequence, number=number))

    # rekurzivni binary search
    print(binary_search_rec(sequence, number, 0, len(sequence)-1))


if __name__ == "__main__":
    my_file = "sequential.json"
    my_number = 90
    main(my_file, my_number)
