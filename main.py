from flask import Flask, render_template, request
from flask_cors import CORS

import reader

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/home')
def home():
    title, comment = reader.get_content()
    return render_template("index.html", title=title, comment=comment)


if __name__ == '__main__':
    app.run(debug=True)