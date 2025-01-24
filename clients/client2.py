# Klient 2 - Pobieranie danych
import requests

def client2():
    url = "http://127.0.0.1:5000/list"
    response = requests.get(url)
    print("[Client 2]", response.json())

if __name__ == "__main__":
    client2()
