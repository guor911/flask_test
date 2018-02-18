from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# @app.error_handlers(404)
# def page_not_found(error):
#     return render_template('404.html'), 404
#
#
# @app.error_handlers(500)
# def internal_server_error(error):
#     return render_template('500.html'), 500


if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(debug=True)

