from flask import Flask, render_template

app = Flask(__name__)


class Items:
    def __init__(self, title, description, price, photo):
        self.title = title
        self.description = description
        self.price = price
        self.photo = photo


@app.route('/')
def home():
    return render_template('base_market.html')


@app.route('/clothes/')
def clothes():
    clothes = [Items('Куртка кожаная', 'Прикольная такая куртка', '1399', "/static/image/jacket.jpg"),
               Items('Свитер', 'Самый крутой свитер на свете', '899', "/static/image/sweater.jpg"),
               Items('Футболка', 'Футболка от Бога', '399', "/static/image/tshirt.jpg"),
               Items('Джинсы', 'Лучше не бывает', '799', "/static/image/jeans.jpg")]
    return render_template('clothes.html', clothes=clothes)


@app.route('/shoes/')
def shoes():
    shoes = [Items('Туфли', 'Будь Богиней', '999', "/static/image/shoes.jpg"),
             Items('Сабо', 'Сабо №1', '599', "/static/image/sabo.jpg"),
             Items('Ботильоны', 'Воу-воу, красавица', '1199', "/static/image/botilions.jpg")]
    return render_template('shoes.html', shoes=shoes)


if __name__ == '__main__':
    app.run(port=5005, debug=True)
