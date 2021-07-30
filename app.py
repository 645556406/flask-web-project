from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)
headers = {
    'Authorization': ''
}
api = 'https://kdsa.cn/request/v1.0'

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/')
def index():
    r = requests.get(api + '/banner', headers=headers)
    lists = r.json()
    return render_template("index.html", lists=lists)


@app.route('/product')
def product():
    r = requests.get(api + '/product', headers=headers)
    lists = r.json()
    return render_template("product.html", lists=lists)


@app.route('/news')
def news():
    page = request.args.get("p", type=int, default=0)
    print(page)
    if page == 0:
        page = 1
    skip = (page-1)*8
    r = requests.get(api + f'/news/?limit=8&skip={skip}', headers=headers)
    lists = r.json()
    return render_template("news.html", lists=lists)


@app.route('/detail')
def detail():
    nid = request.args.get("id")
    r = requests.get(api + '/news/' + nid, headers=headers)
    lists = r.json()
    data = lists['data']
    times = datetime.datetime.utcfromtimestamp(data['_createTime']/1000)
    data['_createTime'] = times.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("detail.html", data=data)


@app.route('/case')
def case():
    page = request.args.get("p", type=int, default=0)
    if page == 0:
        page = 1
    skip = (page-1)*6
    r = requests.get(api + f'/case/?limit=6&skip={skip}', headers=headers)
    lists = r.json()
    return render_template("case.html", lists=lists)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
