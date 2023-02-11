from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.visits = 0
app.bg_color = "white"
app.form_data = []

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        app.form_data.append({"name": name, "message": message})
        return redirect("/form_data")

    app.visits += 1
    return render_template("index.html", message="Hello World", visits=app.visits, bg_color=app.bg_color)

@app.route("/form_data")
def form_data():
    return render_template("form_data.html", form_data=app.form_data)

if __name__ == "__main__":
    app.run()
