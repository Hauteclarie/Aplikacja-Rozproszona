# Aplikacja-Rozproszona
Ta aplikacja demonstruje system rozproszony z centralnym serwerem i dwoma klientami. Serwer obsługuje żądania przechowywania i pobierania danych, podczas gdy klienci komunikują się z serwerem za pomocą RPC (zdalne wywołania procedur) opartego na protokole HTTP.

Komponenty:

Serwer:

Zbudowany przy użyciu Flask.
Udostępnia RESTful endpointy do operacji na danych.

Klienci:

Klient 1: Wysyła dane do serwera.
Klient 2: Pobiera dane z serwera.

Wymagania wstępne

Python 3.9+
Menedżer pakietów pip

Endpointy serwera

1. /add (POST)
Opis: Dodaje element do wspólnego magazynu danych.

2. /list (GET)
Opis: Pobiera wszystkie elementy w magazynie danych.

Potencjalne problemy i rozwiązania

Problem: Współbieżne żądania powodujące konflikty
Rozwiązanie: Użycie wbudowanego mechanizmu wielowątkowości Flask do obsługi wielu żądań jednocześnie. W przypadku krytycznych sekcji można zaimplementować mechanizmy blokad.

Problem: Serwer nie uruchamia się
Rozwiązanie: Upewnij się, że Flask jest zainstalowany, uruchamiając:
pip install Flask

Problem: Klienci nie mogą połączyć się z serwerem
Rozwiązanie: Sprawdź, czy serwer działa pod adresem http://127.0.0.1:5000 i czy endpointy są dostępne.
