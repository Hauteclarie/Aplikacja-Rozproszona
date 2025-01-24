# Klient 1 - Dodawanie danych
import requests

def client1():
    url = "http://127.0.0.1:5000/add"
    payload = {"item": "Test Item from Client 1"}
    response = requests.post(url, json=payload)
    print("[Client 1]", response.json())

if __name__ == "__main__":
    client1()
