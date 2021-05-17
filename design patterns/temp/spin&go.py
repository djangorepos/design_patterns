import numpy as np
from os import listdir


class OpenFile:
    @staticmethod
    def open_file() -> np.ndarray:
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

    def find(self, s, start, end, i, j):
        start_index = s.find(start)
        end_index = s.find(end)
        if ("-1" not in str(start_index)) and ("-1" not in str(end_index)):
            return s[start_index + i:end_index + j]

    @staticmethod
    def hands(hands_array=None, hands_list=None):
        if hands_array is None:
            hands_array = []
        if hands_list is None:
            hands_list = []
        for line in hands_array:
            for string in line:
                if self.find(string, "Hand #", "Tournament #", 6, -2) not in hands_list:
                    hands_list.append(find(string, "Hand #", "Tournament #", 6, -2))
                    hands_array = np.array(hands_list)
                    return hands_array

    @staticmethod
    def play(spin_list=None, spin_array=None):
        if spin_array is None:
            spin_array = []
        if spin_list is None:
            spin_list = []
            for line2 in spin_array:
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
    with open("spin&go.txt", "a") as text:
        print("Client: File created")
    while True:
        open_file()
