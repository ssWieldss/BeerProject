const checkBox = document.getElementById('myCheckBox');
const likes_count = document.getElementById("likes_count");
const img = document.getElementById("like_icon");
const background = document.getElementById("like_back");

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

async function onChange () {
    let array = window.location.href.split("/");
    let pk = array[array.length - 2];
    let data = {beerId: pk};
    let url = "http://127.0.0.1:8000/like/";
    let response;

    if (checkBox.checked){
        data["flag"] = true;
         response = await fetch(url, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                "X-CSRFToken": getCookie("csrftoken")
            },
        })
        if (response.ok){
            changeLikeIcon(true);
        }
    }
    else {
        data["flag"] = false;
         response = await fetch(url, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                "X-CSRFToken": getCookie("csrftoken")
            },
        })
        if (response.ok){
            changeLikeIcon(false);
        }
        }

    if (response.ok){
        change_like_count();
    }
    else {
        let error_data = await response.json();
        alert(error_data["error"]);
    }
}

function changeLikeIcon(flag) {
    if (flag){
        img.src = "../../media/photos/liked.png"
    }
    else {
        img.src = "../../media/photos/unliked.png";
    }
}

async function change_like_count(){
    let array = window.location.href.split("/");
    let pk = array[array.length - 2];
    let url = "http://127.0.0.1:8000/get_likes_count/"+pk+"/";
    let response;
        response = await fetch(url, {
            method: 'GET',
            credentials: 'include',
        })
    if (response.ok){
        json_data = await response.json()
        count_ = json_data.likes_count
        likes_count.innerText = count_
    }
}

setInterval(function() {
            change_like_count();
        }, 3000);



checkBox.addEventListener('change', onChange);