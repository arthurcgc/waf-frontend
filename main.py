from forms import CreateWafForm, DeleteWafForm
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"


@app.route('/create')
def create():
    form = CreateWafForm()
    return render_template('create.html', form=form)

@app.route('/delete')
def delete():
    form = DeleteWafForm()
    return render_template('delete.html', form=form)