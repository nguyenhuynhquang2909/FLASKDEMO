from flask import Flask, render_template, url_for

TEMPLATES_AUTO_RELOAD = True
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = TEMPLATES_AUTO_RELOAD

@app.route("/index")
def index():
    print("Reloading...")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8080)