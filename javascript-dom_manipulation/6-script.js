const character = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Erreur réseau');
    }
    return response.json(); // Traiter la réponse JSON ici
  })
  .then((data) => {
    const { name } = data;
    const result = document.createTextNode(name);
    character.appendChild(result);
  })
  .catch((error) => {
    const newText = document.createTextNode(error.message);
    character.appendChild(newText);
  });
