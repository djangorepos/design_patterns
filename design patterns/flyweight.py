import json
from typing import Dict
from text_to_speech import speak


class Flyweight:
    def __init__(self, shared_state: dict) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: list) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared {s} and unique {u} state.")


class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    @staticmethod
    def get_key(state: Dict) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state) -> Flyweight:
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_of_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="\n")


def add_aircraft_to_database(_factory: FlyweightFactory, plates: str, owner: str,
                             brand: str, model: str, color: str) -> None:
    print("Client: Adding a new aircraft to database.")
    speak("Adding a new aircraft to database")
    flyweight = _factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    factory = FlyweightFactory([
        ["B734", "734", "Boeing 737-400"],
        ["B735", "735", "Boeing 737-500"],
        ["B736", "736", "Boeing 737-600"],
        ["B737", "73G", "Boeing 737-700"],
        ["B738", "738", "Boeing 737-800"],
        ["B739", "739", "Boeing 737-900"],
        ["B741", "741", "Boeing 747-100"],
        ["B741", "74T", "Boeing 747-100"],
    ])

    factory.list_of_flyweights()
    add_aircraft_to_database(
        factory, "Freighter", "Developed into YAL-1 and Dreamlifter", "B741", "74T", "Boeing 747-100")
    add_aircraft_to_database(
        factory, "YAL-1 Large Cargo Freighter", "Deprecated in 2018: no longer flying", "B74D", "74J",
        "Boeing 747-400D")
    factory.list_of_flyweights()
