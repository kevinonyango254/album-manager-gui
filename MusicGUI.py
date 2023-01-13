# Author: Joakim Ringstad
# Date: 2023-01-07
# Description: This file contains the GUI functions for calling methods in cdmethods.py.
# Version: 1.0
# Dependencies: PyQt5, json
# License: -

import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QTableWidgetItem, QTableWidget, QHBoxLayout
# Importera funktionerna från "cd.py"
from cdmethods import add_album, remove_album, update_album, print_albums
from ftpmethods import FTP_JSON_pusher

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
        self.media_format_label = QLabel("Format")
        self.media_format_field = QLineEdit()
        self.notes_label = QLabel("Notes")
        self.notes_field = QLineEdit()
        self.output_field = QTextEdit()
        self.add_button = QPushButton("Add album")
        self.remove_button = QPushButton("Remove album")
        self.update_button = QPushButton("Update album")
        self.print_button = QPushButton('Print All Albums')
        self.table = QTableWidget(len(print_albums()), 6)
        self.upload_button = QPushButton("Upload json to website")

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
        buttons_layout.addWidget(self.media_format_label)
        buttons_layout.addWidget(self.media_format_field)
        buttons_layout.addWidget(self.notes_label)
        buttons_layout.addWidget(self.notes_field)
        buttons_layout.addWidget(self.output_field)
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.remove_button)
        buttons_layout.addWidget(self.update_button)
        buttons_layout.addWidget(self.print_button)
        buttons_layout.addWidget(self.upload_button)

        # Skapa huvudlayouten
        main_layout = QHBoxLayout()
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

        # Sätt bredd för buttons_layout
        buttons_layout_widgets_width = 150
        self.artist_field.setFixedWidth(buttons_layout_widgets_width)
        self.artist_field.setFixedWidth(buttons_layout_widgets_width)
        self.title_field.setFixedWidth(buttons_layout_widgets_width)
        self.year_field.setFixedWidth(buttons_layout_widgets_width)
        self.in_stock_field.setFixedWidth(buttons_layout_widgets_width)
        self.media_format_field.setFixedWidth(buttons_layout_widgets_width)
        self.notes_field.setFixedWidth(buttons_layout_widgets_width)
        self.output_field.setFixedWidth(buttons_layout_widgets_width)
        self.output_field.setFixedHeight(50)
        self.add_button.setFixedWidth(buttons_layout_widgets_width)
        self.remove_button.setFixedWidth(buttons_layout_widgets_width)
        self.update_button.setFixedWidth(buttons_layout_widgets_width)
        self.print_button.setFixedWidth(buttons_layout_widgets_width)
        self.upload_button.setFixedWidth(buttons_layout_widgets_width)

        # Sätt bredd för tabellen
        self.table.setMinimumWidth(800)
        # Anslut gränssnittskomponenter till händelsehanterare
        self.add_button.clicked.connect(self.add_album)
        self.remove_button.clicked.connect(self.remove_album)
        self.update_button.clicked.connect(self.update_album)
        self.print_button.clicked.connect(self.print_all_albums)
        self.upload_button.clicked.connect(self.ftpupload)

        self.print_all_albums()
    def ftpupload(self):
        error = FTP_JSON_pusher()
        msg = "Upload succeed"
        if error != 0:
            msg = "Upload failed!"
        self.output_field.setText(msg)
            
    def add_album(self):
        # Hämta värdena från gränssnittskomponenterna
        title = self.title_field.text()
        artist = self.artist_field.text()
        year = self.year_field.text()
        in_stock = self.in_stock_field.text()
        mediaformat = self.media_format_field.text()
        notes = self.notes_field.text()
        error = 0
        # Anropa add_album()-funktionen från "cd.py"
        error = add_album(title, artist, year, in_stock, mediaformat, notes)
        if error != 0:
            self.output_field.setText("Error already exist: {} - {}".format(title, artist))
        else:
            self.output_field.setText("Added album: {} - {}".format(title, artist))
            self.clear_input_fields()
        # Uppdatera output-fältet

        self.print_all_albums()

    def remove_album(self):
        # Spara index för den markerade raden i en variabel
        selected_row = self.table.currentRow()
        # Läs ut innehållet i cellerna för den markerade raden och spara det i variabler
        artist = self.table.item(selected_row, 0).text()
        title = self.table.item(selected_row, 1).text()
        year = self.table.item(selected_row, 2).text()
        in_stock = self.table.item(selected_row, 3).text()
        mediaformat = self.table.item(selected_row, 4).text()
        notes = self.table.item(selected_row, 5).text()

        # Skriv ut innehållet
        print(title, artist, year, in_stock, mediaformat, notes)

        # Anropa remove_album()-funktionen från "cd.py"
        remove_album(title, artist, mediaformat)

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
        new_mediaformat = self.media_format_field.text()
        new_notes = self.notes_field.text()
        selected_row = self.table.currentRow()

        # Läs ut innehållet i cellerna för den markerade raden och spara det i variabler
        try:
            artist = self.table.item(selected_row, 0).text()
            title = self.table.item(selected_row, 1).text()
            year = self.table.item(selected_row, 2).text()
            in_stock = self.table.item(selected_row, 3).text()
            mediaformat = self.table.item(selected_row, 4).text()
            notes = self.table.item(selected_row, 5).text()
        except:
            self.output_field.setText("Select a row to update")
            return

        if len(new_title) < 1:
            new_title = title
        if len(new_artist) < 1:
            new_artist = artist
        if len(new_year) > 0:
            year = new_year
        if len(new_in_stock) > 0:
            in_stock = new_in_stock
        if len(new_mediaformat) > 0:
            mediaformat = new_mediaformat
        if len(new_notes) > 0:
            notes = new_notes

        # Anropa update_album()-funktionen från "cd.py"
        update_album(title, artist, new_title, new_artist, year, in_stock, mediaformat, notes)

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
        table = QTableWidget(len(album_strings), 6)
        self.table.setHorizontalHeaderLabels(
            ["Artist", "Title", "Year", "In stock", "Format", "Notes"])
        # Loopa igenom album-objekten och lägg till dem i tabellen

        for i, album in enumerate(album_strings):
            # Dela upp album-strängen vid kommatecken och spara resultatet i en lista
            # album_items = album.split(", ")
            self.table.setItem(i, 0, QTableWidgetItem(album['artist']))
            self.table.setItem(i, 1, QTableWidgetItem(album['title']))
            self.table.setItem(i, 2, QTableWidgetItem(str(album['year'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(album['in_stock'])))
            self.table.setItem(i, 4, QTableWidgetItem(str(album['format'])))
            self.table.setItem(i, 5, QTableWidgetItem(str(album['notes'])))
            #self.table.resizeColumnToContents(0)
            #self.table.resizeColumnToContents(1)
            self.table.resizeColumnToContents(2)
            self.table.resizeColumnToContents(3)
            self.table.resizeColumnToContents(4)
            self.table.resizeColumnToContents(5)

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
