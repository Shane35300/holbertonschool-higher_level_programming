const liste = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Erreur réseau');
    }
    return response.json(); // Traiter la réponse JSON ici
  })
  .then((data) => {
    const { results } = data;
    for (const movie of results) {
      const { title } = movie;

      const newLi = document.createElement('li');
      const newText = document.createTextNode(title);
      newLi.appendChild(newText);
      liste.appendChild(newLi);
    }
  })
  .catch((error) => {
    const newLi = document.createElement('li');
    const newText = document.createTextNode(error.message);
    newLi.appendChild(newText);
    liste.appendChild(newLi);
  });
