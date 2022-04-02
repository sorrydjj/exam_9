
function onClick(event) {
    let url = event.target.dataset.url
    let newUrl = ("http://127.0.0.1:8000" + url)
    let divs = document.getElementById("tokens")
    let btn = document.getElementById("buttons")
    btn.remove()
    divs.innerHTML += "<p>Ваша ссылка : " + newUrl +"</p>"
}
