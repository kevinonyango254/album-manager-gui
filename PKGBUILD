pkgname=album-manager-gui
pkgver=1.0
pkgrel=1
pkgdesc="A GUI to keep track of all your albums"
arch=('any')
url="https://github.com/joeraven0/album-manager-gui"
license=('BSD')
depends=()
source=()
md5sums=()

build() {
    cd "$srcdir"
    echo "Building package"
}

package() {
    cd "$srcdir"
    echo "Installing package"
    install -Dm 755 $srcdir/album-manager-gui.sh "$pkgdir/usr/bin/album-manager-gui"
    install -Dm 755 $srcdir/albums.json "$pkgdir/usr/lib/album-manager-gui/albums.json"
    install -Dm 755 $srcdir/cridentials.txt "$pkgdir/usr/lib/album-manager-gui/cridentials.txt"
    install -Dm 755 $srcdir/ftpmethods.py "$pkgdir/usr/lib/album-manager-gui/ftpmethods.py"
    install -Dm 755 $srcdir/MusicGUI.py "$pkgdir/usr/lib/album-manager-gui/MusicGUI.py"
    install -Dm 755 $srcdir/cdmethods.py "$pkgdir/usr/lib/album-manager-gui/cdmethods.py"
    install -Dm 755 $srcdir/album-manager-gui.png "$pkgdir/usr/share/pixmaps/album-manager-gui.png"
    install -Dm 755 $srcdir/album-manager-gui.desktop "$pkgdir/usr/share/applications/album-manager-gui.desktop"
}


