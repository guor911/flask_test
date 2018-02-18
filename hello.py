from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Required
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
moment = Moment(app)


@app.route('/',methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('index.html',
                           form=form,
                           name=name,
                           current_time=datetime.utcnow())


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

class NameForm(Form):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(debug=True)

