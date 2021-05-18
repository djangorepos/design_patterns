from text_to_speech import speak


class HttpHandler:
    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(HttpHandler):
    def handle(self, code):
        if code == 404:
            return "Error 404 Not Found"


class Http500Handler(HttpHandler):
    def handle(self, code):
        if code == 500:
            return "500 Internal Server Error"


class Client:
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print(msg)
                speak(msg)
                break
        else:
            print("HTTP 400 Bad Request")
            speak("HTTP 400 Bad Request")


if __name__ == "__main__":
    client = Client()
    client.add_handler(Http404Handler())
    client.add_handler(Http500Handler())
    client.response(400)  # Код не обработан
    client.response(404)  # Ответ: Страница не найдена
    client.response(500)  # Ответ: Ошибка сервера
