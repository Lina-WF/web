# coding: utf-8

from flask import Flask, request, render_template
from flask_caching import Cache
from p.Website.data import db_session
# from p.Website.data.users import User
from p.Website.data.products import Product

cache = Cache(config={'CACHE_TYPE': 'null'})
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config["CACHE_TYPE"] = "null"
cache.init_app(app)


def main():
    """db_session.global_init("../Website/db/blogs.sqlite")
    product = Product()
    product.title = "Лайтстик BTS"
    product.describtion = "Светящаяся палочка фандома BTS (A.R.M.Y.)"
    product.path_to_img = "пока нет"
    product.price = "1000000"
    product.path_to_img = 'armybomb.jpg'
    session = db_session.create_session()
    session.add(product)
    session.commit()"""
    app.run(port=8000, host='127.0.0.1')


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
