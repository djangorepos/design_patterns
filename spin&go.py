from os import listdir
import numpy as np


def open_file() -> np.ndarray:
    list_of_files = listdir("C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix")
    hand_history = []
    for file in list_of_files:
        with open(f"C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix\\{file}", "r") as lines:
            with open("spin&go.txt", "r") as spingo:
                if spingo.read() not in hand_history:
                    print(spingo.read())
                    hand_history.append(lines.readlines())
    return np.array(hand_history, dtype=object)


def hands(hand, tour, i, j):
    for line1 in spin_go:
        for string in line1:
            hand_index = string.find(hand)
            tour_index = string.find(tour)
            if ("-1" not in str(hand_index)) and ("-1" not in str(tour_index)):
                with open("spin&go.txt", "r") as spin_go_r:
                    if string[hand_index + i:tour_index + j] not in spin_go_r.read():
                        with open("spin&go.txt", "a") as spin_go_txt:
                            spin_go_txt.write(string[hand_index + i:tour_index + j])
                            spin_go_txt.write(" ")


def players(p1, p2, i, j, spin_list=None, spin_array=None):
    if spin_array is None:
        spin_array = []
    if spin_list is None:
        spin_list = []
    with open("spin&go.txt", "a") as spin_go_txt3:
        spin_go_txt3.write("\n")
    for line2 in spin_go:
        for string in line2:
            player_index1 = string.find(p1)
            end_index1 = string.find(p2)
            if ("-1" not in str(player_index1)) and ("-1" not in str(end_index1)):
                keys = string[player_index1 + i: end_index1 + j]
                values = string[end_index1 + 1: end_index1 + 4]
                spin_list.append((keys, values))
            player_index2 = string.find("Dealt to Eat.Twix [")
            if "-1" not in str(player_index2):
                spin_list.append(sorted(string[player_index2 + 19: player_index2 + 24].split(" ")))
            player_index3 = string.find("Eat.Twix")
            end_index3 = string.find("\n")
            if "-1" not in str(player_index3):
                spin_list.append(string[player_index2 + 8: end_index3])
                spin_array = np.array(spin_list, dtype=object)
        for spin in spin_array:
            print(spin, type(spin))


if __name__ == "__main__":
    print("Client: I've got an array:")
    a = 0
    while a >= 0:
        spin_go = open_file()
        hands("Hand #", "Tournament #", 6, -2)
        a += 1
        if a == 1:
            players("Seat", "(", 8, -1)
        else:
            a -= 1
