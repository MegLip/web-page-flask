from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekretnyklucz'


@app.route('/')
def main():
    return render_template("base.html")


@app.route('/mypage/me')
def me():
    return render_template("me.html")


@app.route('/mypage/contact')
def contact():
    return render_template("contact.html")


@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        message = request.form.get("message")
        flash('Twoja wiadomość {} została wysłana!'.format(message))
        return redirect('/mypage/contact')


if __name__ == '__main__':
    app.run()
