from flask import Flask

app = Flask(__name__)
counter = 0

@app.route("/")
def hello():
    global counter
    counter += 1
    return "Hello, World! This page has been visited {} times.".format(counter)

if __name__ == "__main__":
    app.run(debug=True)
