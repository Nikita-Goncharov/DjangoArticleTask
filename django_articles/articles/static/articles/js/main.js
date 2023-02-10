console.log('hello')

const searchField = document.querySelector('.search_field')
const container = document.querySelector('.container')

// From django docs
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrftoken = getCookie('csrftoken');
let request = new XMLHttpRequest();

function search() {
    request.open('POST', '/');

    request.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
          let articlesSrting = JSON.parse(this.responseText)['filtered_articles']
          let articles = JSON.parse(articlesSrting)
          console.log(articles)
          for (let article of articles) {
              console.log(article)
              container.innerHTML = ''
              container.innerHTML += `
              <div class="article">
                    <div>
                        <a href="/article_detail/${article.pk}/"><h2>Title:  ${article['fields']['title']} </h2></a>
                        <h3>Author: ${article['fields']['author']}</h3>
                        <h4>Date: ${article['fields']['created_date']}</h4>
                    </div>
              </div>
              `
          }

      }
    }
    request.setRequestHeader("X-CSRFToken", csrftoken);
    request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
    request.send(searchField.value);
    searchField.value = ''
}
