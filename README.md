# Album Manager GUI

This is a graphical user interface (GUI) application for managing a list of music albums. The user can add, remove, and update albums, and view the list of all albums. The application is built using PyQt5 and stores the list of albums in a file called 'albums.json'.

FTP upload feature enables to push albums.json to a webserver. Index.html & javascript to load json data to website also uploaded.

Fun fact: Started as a try-out for coding with chatGPT-3 but grew bigger.

![Album Manager GUI](gitassets/Screenshot_20230113_202609.png)

Figure 1 - Run MusicGUI.py graphical user interface to manipulate JSON

![Album Manager Website](gitassets/Screenshot_20230113_203503.png)

Figure 2 - Web server loading albums.json

![Album Manager Flow](gitassets/Screenshot_20230113_211255.png)
Figure 3 - Transmit albums.json over FTP by GUI button "Upload json to website"

## Prerequisites

- PyQt5
- json

## Installation

1. Clone the repository

```bash
git clone https://github.com/joeraven0/album-manager-gui.git

```
2. Install the dependencies

```bash
pip install pyqt5 json
```
3. Setup FTP cridentials in cridentials.txt (optional for publishing online)

  * cridentials.txt

4. Upload to web server (optional for publishing online)

  * index.html
  * styles.css
  * albums.js
  * albums.json (or upload through gui)

5. Run the script

```bash
python MusicGUI.py
```

## Usage

1. Enter the artist, title, year, and number of copies in stock for the album you want to add.
2. Click the "Add album" button to add the album to the list.
3. To remove an album, select the album in the table and click the "Remove album" button.
4. To update an album, select the album in the table, make the necessary changes in the input fields, and click the "Update album" button.
5. To view the list of all albums, click the "Print All Albums" button.
6. Upload through FTP, click the "Upload json to website" button. (optional)

## License

Free for everyone, always. Microsoft have to pay.
