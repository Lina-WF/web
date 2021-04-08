# coding: utf-8

from flask import Flask, request, render_template
from flask import Flask
from p.Website.data import db_session
from p.Website.data.users import User
from p.Website.data.products import Product

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("../Website/db/blogs.sqlite")
    app.run(port=8080, host='127.0.0.1')
    """product = Product()
    product.title = "Лайтстик BTS"
    product.describtion = "Светящаяся палочка фандома BTS (A.R.M.Y.)"
    product.path_to_img = "пока нет"
    product.price = "1000000"
    session = db_session.create_session()
    dlt = session.query(Product).first()
    dlt.path_to_img = 'armybomb.png'
    session.commit()"""


@app.route('/')
@app.route('/kpopshop', methods=['POST', 'GET'])
def main_wind():
    if request.method == "POST":
        print(request.form['filter'])
        return render_template('main.html')
    else:
        session = db_session.create_session()
        product = session.query(Product).first()
        return render_template('main.html', path_to_img="../static/img/" + product.path_to_img, pr_title=product.title)


if __name__ == '__main__':
    main()
