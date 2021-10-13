from logging import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
<<<<<<< HEAD


if __name__ == '__main__':
    app.run()
=======
>>>>>>> main
