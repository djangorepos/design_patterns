from googletrans import Translator
from text_to_speech import speak


class Target:

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    @staticmethod
    def specific_request() -> str:
        return ".meht dne gnisoppo yb dnA selbuort fo aes a tsniaga smra ekat ot rO ,enutrof suoegartuo fo sworra dna " \
               "sgnils ehT reffus ot dnim eht ni relbon sit' rehtehW :noitseuq eht si taht ,eb ot ton ro ,eb oT "


class Adapter(Target, Adaptee):

    def request(self) -> str:
        return f"Adapter: (INVERSE) {self.specific_request()[::-1]}"


def client_code(_target: Target) -> str:
    return _target.request()


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    speak("I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    speak("The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n")
    print("Client: But I can work with it via the Adapter:")
    speak("But I can work with it via the Adapter:")
    adapter = Adapter()
    print(client_code(adapter))
    translator = Translator()
    result = translator.translate(client_code(adapter), dest="ru")
    print(f"Translator: (TRANSLATE) {str(result)[42:241:]}")
