from flask import Flask, render_template
import requests
import os

app = Flask(__name__)  # Nova instância da classe Flask


@app.route('/')  # Mapeamento URL
def borad_archive():

    username = 'juliana.goncalves@corp.globo.com'
    password = 'Admin1234'
    url_api = "https://produtos-globocom.leankit.com/kanban/api/board/196166479/archive"

    http = requests.Session()
    http.auth = (username, password)
    response = http.get(url_api).json()  # dicionario python

    board_datas = response

    cards_esp2 = board_datas['ReplyData'][0][0]['ChildLanes'][2]['Lane']['Cards']

    title = board_datas['ReplyData'][0][0]['ChildLanes'][2]['Lane']['Title']

    return render_template('board.html', title=title, cards=cards_esp2)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
