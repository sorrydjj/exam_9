function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function onClickPhoto(event) {
    let csrftokens = getCookie('csrftoken');
    let url = event.target.dataset.url
    let pk = event.target.dataset.pk
    let response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftokens
        }
    })
    let answer = await response.json();
    if (answer["status"] === "add") {
        event.target.innerText = "Удалить из избранного "
        event.target.dataset.url = "/favorite/photo/delete/" + pk + "/"
        event.target.style.background = "red"
    }
    if (answer["status"] === "delete") {
        event.target.innerText = "Добавить в избранное "
        event.target.dataset.url = "/favorite/photo/add/" + pk + "/"
        event.target.style.background = "green"
    }

}