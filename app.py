from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.visits = 0
app.bg_color = "white"

@app.route("/")
def hello():
    app.visits += 1
    return render_template("index.html", message="Hello World", visits=app.visits, bg_color=app.bg_color)

@app.route("/api/data")
def data():
    data = {
        "message": "Hello World",
        "visits": app.visits,
        "background_color": app.bg_color
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()
