class Target:

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    @staticmethod
    def specific_request() -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(_target: "Target") -> None:
    print(_target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
