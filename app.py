from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def first_flask():  # put application's code here
    print('this is my try in flask')
    return 'This is my first flask EVER!!!'

@app.route('/redirect_use')
def redirect_usage():  # put application's code here
    return redirect('/')

@app.route('/home')
def home():  # put application's code here
    return redirect(url_for('redirect_usage'))


if __name__ == '__main__':
    app.run()
