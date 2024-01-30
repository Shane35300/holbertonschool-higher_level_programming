document.addEventListener('DOMContentLoaded', () => {
  const hello = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Erreur réseau');
      }
      return response.json(); // Traiter la réponse JSON ici
    })
    .then((data) => {
      const word = data.hello;

      const newText = document.createTextNode(word);
      hello.appendChild(newText);
    })
    .catch((error) => {
      const newText = document.createTextNode(error.message);
      hello.appendChild(newText);
    });
});
