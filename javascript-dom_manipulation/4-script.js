const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', () => {
  const newLi = document.createElement('li');
  const newText = document.createTextNode('Item');
  newLi.appendChild(newText);
  myList.appendChild(newLi);
});
