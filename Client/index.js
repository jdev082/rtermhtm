document.querySelector('#rbtn').addEventListener("click", function() {
    cmd = document.querySelector('#input').value
    fetch(`http://127.0.0.1:5000?cmd=${cmd}`)
    .then(x => x.text())
    .then(y => display(y, cmd));
});

function display(y, c) {
    e = document.createElement('p')
    e.innerText = `$ ${c}\n\n${y}`
    document.body.appendChild(e)
}