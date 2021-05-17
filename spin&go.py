from time import sleep

import numpy as np
from os import listdir


def open_file(files) -> np.ndarray:
    hand_history = []
    for file in files:
        with open(f"C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix\\{file}", "r") as lines:
            with open("spin&go_hands.txt", "r") as spingo:
                if spingo.read() not in hand_history:
                    print(spingo.read())
                    hand_history.append(lines.readlines())
    return np.array(hand_history, dtype=object)


def hands():
    for line1 in spin_go:
        for string in line1:
            hand_index = string.find("Hand #")
            tour_index = string.find("Tournament #")
            if ("-1" not in str(hand_index)) and ("-1" not in str(tour_index)):
                with open("spin&go_hands.txt", "r") as spin_go_r:
                    if string[hand_index + 6:tour_index - 2] not in spin_go_r.read():
                        with open("spin&go_hands.txt", "a") as spin_go_txt:
                            spin_go_txt.write(string[hand_index + i:tour_index + j])
                            spin_go_txt.write(" ")
                    return True


def play(flag, spin_list=None, spin_array=None):
    if spin_array is None:
        spin_array = []
    if spin_list is None:
        spin_list = []
    if flag:
        for line2 in spin_go:
            for string in line2:
                start_index = string.find("Seat")
                end_index = string.find("(")
                if ("-1" not in str(start_index)) and ("-1" not in str(end_index)):
                    keys = string[start_index + 8: end_index - 1]
                    values = string[end_index + 1: end_index + 4]
                    spin_list.append((keys, values))
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

        spin_array = np.array(spin_list, dtype=object)
    for spin in spin_array:
        print(spin, type(spin))
    return spin_array


if __name__ == "__main__":
    print("Client: I've got an array:")
    set_of_files = set(listdir("C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix"))
    set_of_old_files = set(listdir("C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix"))
    spin_go = open_file(set_of_old_files)
    hands()
    play(hands)
    while True:
        set_of_files = set(listdir("C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix"))
        if set_of_old_files - set_of_files not in set():
            spin_go = open_file(set_of_files)
        flag = hands()
        play(flag)
        flag = False
        sleep(10)
