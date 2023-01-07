# Author: Joakim Ringstad
# Date: 2023-01-07
# Description: This file contains the GUI functions for calling methods in cdmethods.py.
# Version: 1.0
# Dependencies: PyQt5, json
# License: MIT

import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QTableWidgetItem, QTableWidget, QHBoxLayout
# Importera funktionerna från "cd.py"
from cdmethods import add_album, remove_album, update_album, print_albums


class AlbumManager(QWidget):
    def __init__(self):
        super().__init__()

        # Skapa gränssnittskomponenter
        self.artist_label = QLabel("Artist:")
        self.artist_field = QLineEdit()
        self.title_label = QLabel("Title:")
        self.title_field = QLineEdit()
        self.year_label = QLabel("Year:")
        self.year_field = QLineEdit()
        self.in_stock_label = QLabel("In stock:")
        self.in_stock_field = QLineEdit()
        self.output_field = QTextEdit()
        self.add_button = QPushButton("Add album")
        self.remove_button = QPushButton("Remove album")
        self.update_button = QPushButton("Update album")
        self.print_button = QPushButton('Print All Albums')
        self.table = QTableWidget(len(print_albums()), 4)

        # Skapa layouten för knapparna och fälten
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.artist_label)
        buttons_layout.addWidget(self.artist_field)
        buttons_layout.addWidget(self.title_label)
        buttons_layout.addWidget(self.title_field)
        buttons_layout.addWidget(self.year_label)
        buttons_layout.addWidget(self.year_field)
        buttons_layout.addWidget(self.in_stock_label)
        buttons_layout.addWidget(self.in_stock_field)
        buttons_layout.addWidget(self.output_field)
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.remove_button)
        buttons_layout.addWidget(self.update_button)
        buttons_layout.addWidget(self.print_button)

        # Skapa huvudlayouten
        main_layout = QHBoxLayout()
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)
        self.table.setMinimumWidth(500)
        # Anslut gränssnittskomponenter till händelsehanterare
        self.add_button.clicked.connect(self.add_album)
        self.remove_button.clicked.connect(self.remove_album)
        self.update_button.clicked.connect(self.update_album)
        self.print_button.clicked.connect(self.print_all_albums)

        self.print_all_albums()

    def add_album(self):
        # Hämta värdena från gränssnittskomponenterna
        title = self.title_field.text()
        artist = self.artist_field.text()
        year = self.year_field.text()
        in_stock = self.in_stock_field.text()

        # Anropa add_album()-funktionen från "cd.py"
        add_album(title, artist, year, in_stock)

        # Uppdatera output-fältet
        self.output_field.setText("Added album: {} - {}".format(title, artist))
        self.clear_input_fields()
        self.print_all_albums()

    def remove_album(self):
        # Spara index för den markerade raden i en variabel
        selected_row = self.table.currentRow()

        # Läs ut innehållet i cellerna för den markerade raden och spara det i variabler
        artist = self.table.item(selected_row, 0).text()
        title = self.table.item(selected_row, 1).text()
        year = self.table.item(selected_row, 2).text()
        in_stock = self.table.item(selected_row, 3).text()

        # Skriv ut innehållet
        print(title, artist, year, in_stock)

        # Anropa remove_album()-funktionen från "cd.py"
        remove_album(title, artist)

        # Uppdatera output-fältet
        self.output_field.setText(
            "Removed album: {} - {}".format(title, artist))
        self.clear_input_fields()
        self.print_all_albums()

    def update_album(self):
        # Hämta värdena från gränssnittskomponenterna
        new_title = self.title_field.text()
        new_artist = self.artist_field.text()
        new_year = self.year_field.text()
        new_in_stock = self.in_stock_field.text()
        selected_row = self.table.currentRow()

        # Läs ut innehållet i cellerna för den markerade raden och spara det i variabler
        artist = self.table.item(selected_row, 0).text()
        title = self.table.item(selected_row, 1).text()
        year = self.table.item(selected_row, 2).text()
        in_stock = self.table.item(selected_row, 3).text()

        if len(new_title) < 1:
            new_title = title
        if len(new_artist) < 1:
            new_artist = artist
        if len(new_year) > 0:
            year = new_year
        if len(new_in_stock) > 0:
            in_stock = new_in_stock

        # Anropa update_album()-funktionen från "cd.py"
        update_album(title, artist, new_title, new_artist, year, in_stock)

        # Uppdatera output-fältet
        self.output_field.setText(
            "Updated album: {} - {}".format(new_title, new_artist))
        self.clear_input_fields()
        self.print_all_albums()

    def print_all_albums(self):
        # Anropa print_albums()-funktionen från cd.py och spara resultatet i en variabel
        album_strings = print_albums()
        rowPosition = self.table.rowCount()
        self.table.clearContents()
        print('Row count: '+str(rowPosition))
        # Lägg till eller ta bort rader ur tabellen
        if rowPosition < len(album_strings):
            rowPosition = self.table.rowCount()
            self.table.insertRow(rowPosition)
        if rowPosition > len(album_strings):
            rowPosition = self.table.rowCount()
            self.table.removeRow(self.table.rowCount()-1)

        # Dela upp album-strängarna vid radbrytningar och spara resultatet i en lista
        # album_list = album_strings.split("\n")
        print(len(album_strings))
        # Skapa en QTableWidget med rätt antal rader och kolumner
        table = QTableWidget(len(album_strings), 4)
        self.table.setHorizontalHeaderLabels(
            ["Artist", "Title", "Year", "In stock"])
        # Loopa igenom album-objekten och lägg till dem i tabellen

        for i, album in enumerate(album_strings):
            # Dela upp album-strängen vid kommatecken och spara resultatet i en lista
            # album_items = album.split(", ")
            self.table.setItem(i, 0, QTableWidgetItem(album['artist']))
            self.table.setItem(i, 1, QTableWidgetItem(album['title']))
            self.table.setItem(i, 2, QTableWidgetItem(str(album['year'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(album['in_stock'])))
            self.table.resizeColumnToContents(0)
            self.table.resizeColumnToContents(1)
            self.table.resizeColumnToContents(2)
            self.table.resizeColumnToContents(3)

    def clear_input_fields(self):
        self.title_field.clear()
        self.artist_field.clear()
        self.year_field.clear()
        self.in_stock_field.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    manager = AlbumManager()
    manager.show()

    sys.exit(app.exec_())
