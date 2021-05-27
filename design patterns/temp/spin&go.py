import numpy as np
from os import listdir


def open_files() -> np.ndarray:
    hand_history = []
    list_of_files = listdir("C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix")
    for file in list_of_files:
        with open("spin&go.txt", "r") as history:
            if file[13:22] not in history.readline():
                print("Client: I've got an array:")
                with open("spin&go.txt", "a") as history_files:
                    history_files.write(file[13:22])
                    history_files.write(" ")
                    with open(f"C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix\\{file}",
                              "r") as lines:
                        hand_history.append(lines.readlines())
    return np.array(hand_history, dtype=object)


def find_str(s, start, end, i, j):
    start_index = s.find(start)
    end_index = s.find(end)
    if ("-1" not in str(start_index)) and ("-1" not in str(end_index)):
        return s[start_index + i:end_index + j]


def play(spin_array=None, spin_list=None, spin_dict=None):
    if spin_array is None:
        spin_array = []
    if spin_list is None:
        spin_list = []
    if spin_dict is None:
        spin_dict = {}
        for line in spin_array:
            for string in line:
                start_index = string.find("Seat")
                end_index = string.find("(")
                if ("-1" not in str(start_index)) and ("-1" not in str(end_index)):
                    key = string[start_index + 8: end_index - 1]
                    value = string[end_index + 1: end_index + 4]
                    spin_dict.update({key: value})
                start_index = string.find("Dealt to Eat.Twix [")
                if "-1" not in str(start_index):
                    spin_list.append(sorted(string[start_index + 19: start_index + 24].split(" ")))
                start_index = string.find("Eat.Twix")
                end_index = string.find("\n")
                if "-1" not in str(start_index):
                    spin_list.append(string[start_index: end_index])
                start_index = string.find("*** FLOP *** [")
                if "-1" not in str(start_index):
                    spin_list.append(sorted(string[start_index + 14: start_index + 22].split(" ")))
                start_index = string.find("*** TURN *** [")
                if "-1" not in str(start_index):
                    spin_list.append(sorted(string[start_index + 25: start_index + 27].split(" ")))
                start_index = string.find("*** RIVER *** [")
                if "-1" not in str(start_index):
                    spin_list.append(sorted(string[start_index + 29: start_index + 31].split(" ")))
            print(spin_dict)
            print(spin_list)
            spin_list = []


if __name__ == "__main__":
    with open("spin&go.txt", "w") as text:
        print("Client: File created")
        play(open_files())
