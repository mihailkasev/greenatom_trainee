from http.client import HTTPConnection


def find_your_ip() -> str:
    """Направляет GET-запрос ifconfig.me/ip и возвращает IP адрес в формате utf-8. """
    conn = HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    public_ip = conn.getresponse().read().decode('utf-8')
    return public_ip
