fetch('albums.json')
  .then(response => response.json())
  .then(data => {
    // sortera album efter artist
    data.sort((a, b) => (a.artist > b.artist) ? 1 : -1);

    // loopa igenom alla album och skapa HTML-element för varje album
    let albumHTML = data.map(album => `
      <tr>
        <td>${album.title}</td>
        <td>${album.artist}</td>
        <td>${album.year}</td>
        <td>${album.in_stock}</td>
        <td>${album.format}</td>
        <td>${album.notes}</td>
      </tr>
    `).join('');

    // lägg till HTML-elementen i album-container
    const albumContainer = document.getElementById('album-container');
    albumContainer.innerHTML = albumHTML;

    // hämta sök-input och sök-knapp
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');

  
  // lägg till eventlyssnare på sök-input
  searchInput.addEventListener('keyup', (event) => {
    // om Enter-knappen trycks ner
    if (event.keyCode) {
      // utlös sök-knappens click-event
      searchButton.click();
    }
  });
    const headings = document.querySelectorAll('th');

headings.forEach(heading => {
  heading.addEventListener('click', () => {
    // hämta data-sort attributet från den klickade kolumnrubriken
    const sortBy = heading.getAttribute('data-sort');

    // sortera albumen med hjälp av sort()
    data.sort((a, b) => (a[sortBy] > b[sortBy]) ? 1 : -1);

    // skapa och lägg till HTML för de sorterade albumen
    albumHTML = data.map(album => `
      <tr>
        <td>${album.title}</td>
        <td>${album.artist}</td>
        <td>${album.year}</td>
        <td>${album.in_stock}</td>
        <td>${album.format}</td>
        <td>${album.notes}</td>
      </tr>
    `).join('');
    albumContainer.innerHTML = albumHTML;
  });
});

    // lägg till eventlyssnare på sök-knappen
    searchButton.addEventListener('click', () => {
      // hämta söksträngen
      const searchString = searchInput.value.toLowerCase();

      // filtrera albumen och skapa ny HTML
      albumHTML = data
        .filter(album => album.artist.toLowerCase().includes(searchString) || album.title.toLowerCase().includes(searchString))
        .map(album => `
          <tr>
            <td>${album.title}</td>
            <td>${album.artist}</td>
            <td>${album.year}</td>
            <td>${album.in_stock}</td>
            <td>${album.format}</td>
            <td>${album.notes}</td>
          </tr>
        `)
        .join('');

      // ersätt HTML i album-container med den nya HTML-koden
      albumContainer.innerHTML = albumHTML;

    })
    
  });