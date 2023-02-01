from flask import Flask, render_template

app = Flask(__name__)  # this is an object of Flask


@app.route('/')  # redirect to the first page to the app
def home():
    return render_template('/index.html')


if __name__ == "__main__":
    app.run(debug=True)  # to activate app server
