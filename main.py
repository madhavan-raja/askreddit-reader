from flask import Flask, render_template, request

import reader

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    title, comment = reader.get_content()
    return render_template("index.html", title=title, comment=comment)


if __name__ == '__main__':
    app.run(debug=True)
