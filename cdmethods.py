# Author: Joakim Ringstad
# Date: 2023-01-07
# Description: This file contains functions for manipulating a list of music albums in albums.json.
# Version: 1.0
# Dependencies: json
# License: -

import json

# Funktionen tar in parametrarna "title", "artist", "year" och "in_stock" som är värdena för album-objektet


def add_album(title, artist, year, in_stock):
    # Öppna filen "albums.json" i läge "r" (read) för att läsa in innehållet
    with open("albums.json", "r") as file:
        # Läs in innehållet och omvandla det till en Python-lista
        albums = json.load(file)

    # Loopa igenom listan "albums" och leta efter ett album-objekt med rätt titel och artist
    for album in albums:
        # Om titeln och artisten på album-objektet matchar sökningen, avbryt funktionen
        if album["title"] == title and album["artist"] == artist:
            return

    # Skapa ett nytt album-objekt med hjälp av parametrarna
    new_album = {
        "title": title,
        "artist": artist,
        "year": year,
        "in_stock": in_stock
    }

    # Lägg till det nya album-objektet till listan "albums"
    albums.append(new_album)

    # Öppna filen "albums.json" i läge "w" (write) för att skriva till den
    with open("albums.json", "w") as file:
        # Formatera den uppdaterade listan som en json-sträng med indenterat innehåll och radbrytningar
        sorted_albums = sorted(albums, key=lambda album: album["artist"])
        formatted_json = json.dumps(
            sorted_albums, indent=4, separators=(',', ': '))

        # Skriv den formaterade strängen till filen
        file.write(formatted_json)


# Funktionen tar in parametrarna "title" och "artist" som är titeln och artisten på det album som ska tas bort
def remove_album(title, artist):
    # Öppna filen "albums.json" i läge "r" (read) för att läsa in innehållet
    with open("albums.json", "r") as file:
        # Läs in innehållet och omvandla det till en Python-lista
        albums = json.load(file)

    # Loopa igenom listan "albums" och leta efter ett album-objekt med rätt titel och artist
    for album in albums:
        # Om titeln och artisten på album-objektet matchar sökningen, ta bort det från listan
        if album["title"] == title and album["artist"] == artist:
            albums.remove(album)
            break

    # Öppna filen "albums.json" i läge "w" (write) för att skriva till den
    with open("albums.json", "w") as file:
        # Formatera den uppdaterade listan som en json-sträng med indenterat innehåll och radbrytningar
        sorted_albums = sorted(albums, key=lambda album: album["artist"])
        formatted_json = json.dumps(
            sorted_albums, indent=4, separators=(',', ': '))
        # Skriv den formaterade strängen till filen
        file.write(formatted_json)


# Funktionen tar in parametrarna "title", "artist", "new_title", "new_artist", "year" och "in_stock" som är de nya värdena för album-objektet
def update_album(title, artist, new_title, new_artist, year, in_stock):
    # Öppna filen "albums.json" i läge "r" (read) för att läsa in innehållet
    with open("albums.json", "r") as file:
        # Läs in innehållet och omvandla det till en Python-lista
        albums = json.load(file)

    # Loopa igenom listan "albums" och leta efter ett album-objekt med rätt titel och artist
    for album in albums:
        # Om titeln och artisten på album-objektet matchar sökningen, ändra värdena på album-objektet
        if album["title"] == title and album["artist"] == artist:
            album["title"] = new_title
            album["artist"] = new_artist
            album["year"] = year
            album["in_stock"] = in_stock
            break

    # Öppna filen "albums.json" i läge "w" (write) för att skriva till den
    with open("albums.json", "w") as file:
        # Formatera den uppdaterade listan som en json-sträng med indenterat innehåll och radbrytningar
        sorted_albums = sorted(albums, key=lambda album: album["artist"])
        formatted_json = json.dumps(
            sorted_albums, indent=4, separators=(',', ': '))
        # Skriv den formaterade strängen till filen
        file.write(formatted_json)


def print_albums():
    # Öppna filen "albums.json" i läge "r" (read) för att läsa in innehållet
    with open("albums.json", "r") as file:
        # Läs in innehållet och omvandla det till en Python-lista
        albums = json.load(file)

    # Skapa en tom sträng för att spara informationen om albumen
    albums_string = ""

    # Loopa igenom listan "albums" och lägg till information om varje album i strängen
    for album in albums:
        album_string = "{} - {} ({}, in stock: {})\n".format(
            album["artist"], album["title"], album["year"], album["in_stock"])
        albums_string += album_string

    # Returnera strängen med information om albumen
    return albums
