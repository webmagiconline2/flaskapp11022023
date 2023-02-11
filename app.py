from flask import Flask

app = Flask(__name__)
counter = 0

@app.route("/")
def hello():
    global counter
    counter += 1
    return '''
    <html>
    <head>
        <style>
            body {{
                background-color: lightblue;
            }}
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This page has been visited {} times.</p>
    </body>
    </html>
    '''.format(counter)

if __name__ == "__main__":
    app.run(debug=True)
